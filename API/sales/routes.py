from datetime import datetime, timedelta
from API.models import Sale
from flask import Blueprint, jsonify, request
from API import db, bcrypt
from API.lib.auth import business_login_required
from API.lib.data_serializer import serialize_sale

sales_blueprint = Blueprint("sales", __name__, url_prefix="/API/sales")


@sales_blueprint.route("/add-sale", methods=["POST"])
@business_login_required
def record_sale(business):
    """
        Record new Sales
        :param business: Business making the sale
        :return: 200, 400
    """
    payload = request.get_json()
    payment_method = payload["paymentMethod"].strip()
    description = payload["description"].strip()
    service_id = payload["serviceId"]

    if not business.active:
        return jsonify({"message": "You need to activate your account first."}), 400

    business_services = [service.id for service in business.services.all()]
    if service_id not in business_services:
        return jsonify({"message": "We are not offering this service at the moment"}), 400

    sale = Sale(
        payment_method=payment_method,
        description=description,
        service_id=service_id,
        business_id=business.id
    )

    db.session.add(sale)
    db.session.commit()

    return jsonify({"message": "Sale Added", "newSale": serialize_sale(sale)}), 200


@sales_blueprint.route("/all", methods=["GET"])
@business_login_required
def fetch_all_business_sales(business):
    """
        Fetch all the sales for a given business
        :param business: Business
        :return:
    """

    sales = Sale.query.filter_by(business_id=business.id).all()
    all_sales = []

    for sale in sales:
        sale_info = serialize_sale(sale)
        sale_info["service"] = sale.service.service
        all_sales.append(sale_info)

    return jsonify({"message": "Sales", "sales": all_sales})


@sales_blueprint.route("/delete/<int:sale_id>", methods=["DELETE"])
@business_login_required
def delete_sale(business, sale_id):
    """
        Delete a sale
        :param business:
        :param sale_id:
        :return: 404, 400, 200
    """
    payload = request.get_json()
    password = payload["password"].strip()

    if not bcrypt.check_password_hash(business.password, password):
        return jsonify({"message": "Incorrect password"}), 401

    sale = Sale.query.get(sale_id)

    if not sale:
        return jsonify({"message": "Not found"}), 404

    if business.id != sale.business_id:
        return jsonify({"message": "Not allowed"}), 400

    db.session.delete(sale)
    db.session.commit()

    return jsonify({"message": "Sale deleted"})


@sales_blueprint.route("/analysis", methods=["GET"])
@business_login_required
def revenue_analytics(business):
    """
        Business Revenue Analysis
        :param business: Logged in Business
        :return: 200
    """
    today = datetime.today().date()
    current_month = today.month
    current_year = today.year
    sales = business.sales.all()
    seven_days_ago = today - timedelta(days=7)

    lifetime_sales = []
    total_sales = 0
    current_month_revenue = 0
    last_seven_days_sales = 0

    for sale in sales:
        service = sale.service
        serialized_sale = serialize_sale(sale)
        serialized_sale["price"] = service.price
        lifetime_sales.append(serialized_sale)
        total_sales += service.price
        if sale.date_created.date().month == current_month and sale.date_created.date().year == current_year:
            current_month_revenue += service.price
        if sale.date_created.date() > seven_days_ago:
            last_seven_days_sales += service.price

    return jsonify(
        {
            "message": "Success",
            "lifetime_sales": lifetime_sales,
            "total_sales": total_sales,
            "current_month_revenue": current_month_revenue,
            "last_seven_days": last_seven_days_sales
        }
    ), 200

