from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_cors import CORS
from flask_migrate import Migrate
from API.config import Config
from dotenv import load_dotenv


db = SQLAlchemy()
mail = Mail()
bcrypt = Bcrypt()
migrate = Migrate()
cors = CORS()


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, supports_credentials=True)

    from API.clients.routes import clients_blueprint
    from API.appointments.routes import appointment_blueprint
    from API.businesses.routes import business_blueprint
    from API.reviews.routes import reviews_blueprint
    from API.ratings.routes import ratings_blueprint
    from API.notifications.routes import notifications_blueprint
    from API.sales.routes import sales_blueprint
    from API.expense_accounts.routes import accounts_blueprint
    from API.expenses.routes import expenses_blueprint
    from API.inventory.routes import inventory_blueprint
    from API.staff.routes import staff_blueprint
    from API.services.routes import services_blueprint
    from API.admin.routes import admin_blueprint
    from API.messaging.routes import messaging_blueprint

    app.register_blueprint(clients_blueprint)
    app.register_blueprint(appointment_blueprint)
    app.register_blueprint(business_blueprint)
    app.register_blueprint(reviews_blueprint)
    app.register_blueprint(ratings_blueprint)
    app.register_blueprint(notifications_blueprint)
    app.register_blueprint(sales_blueprint)
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(expenses_blueprint)
    app.register_blueprint(inventory_blueprint)
    app.register_blueprint(staff_blueprint)
    app.register_blueprint(services_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(messaging_blueprint)

    return app
