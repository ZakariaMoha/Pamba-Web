from flask_mail import Message
from API import mail
from flask import render_template


def send_otp(recipient, otp, name):
    """
        Send account verification OTP
        :param recipient: Recipient Email
        :param name: Client name
        :param otp: OTP value
        :return: None
    """
    message = Message("[Action Required]: Verify Account - PAMBA", sender="pamba.africa", recipients=[recipient])
    message.html = render_template("otp.html", name=name, code=otp)
    mail.send(message)


def send_reset_email(recipient, token, name):
    """
        Send password reset token for businesses
        :param recipient: User Email
        :param token: JWT Token
        :param name: User's name
        :return:
    """
    reset_url = f"https://www.pamba.africa/reset-password/{token}"
    message = Message("Reset Password - PAMBA", sender="pamba.africa", recipients=[recipient])
    message.html = render_template("reset.html", url=reset_url, name=name)
    mail.send(message)


def sent_client_reset_token(recipient, token, name):
    """
        Send password reset token for clients
        :param recipient: User Email
        :param token: JWT Token
        :param name: User's name
        :return:
    """
    message = Message("Reset Password - PAMBA", sender="pamba.africa", recipients=[recipient])
    message.html = render_template("clientReset.html", token=token, name=name)
    mail.send(message)


def business_account_activation_email(recipient, token, name):
    """
        Send the account verification URL to businesses upon account creation.
        :param recipient: Recipient Email Address.
        :param token: Verification Token.
        :param name: Business Name.
        :return:
    """
    url = f"https://www.pamba.africa/verify/{token}"
    message = Message("[Action Required]: Activate your Pamba account", sender="pamba.africa", recipients=[recipient])
    message.html = render_template("activatebusiness.html", name=name, url=url)
    mail.send(message)


def appointment_confirmation_email(client_name, date, time, business_location, business_name, business_directions, recipient):
    """
        Send email notification for successful appointment booking
        :param recipient: Client email
        :param client_name: Name of the client
        :param date: Appointment Date
        :param time: Appointment Time
        :param business_location: Business Location
        :param business_name: Name of the Business
        :param business_directions: Direction to the Business Location
        :return:
    """
    message = Message("Pamba - New Appointment", sender="pamba.africa", recipients=[recipient])
    message.html = render_template(
        "confirmAppointment.html",
        name=client_name if client_name else None,
        appointment_date=date,
        appointment_time=time,
        business_location=business_location,
        business_name=business_name,
        business_direction=business_directions
    )
    mail.send(message)


def send_ask_for_review_mail(url, name, business_name, recipient):
    """
        Ask clients to review
        :param url: Review url
        :param name: client name if any
        :param business_name: Name of Business
        :param recipient: Client Email
        :return:
    """
    message = Message("Pamba - Review your Appointment", sender="pamba.africa", recipients=[recipient])
    message.html = render_template(
        "askForReview.html",
        url=url,
        name=name,
        business_name=business_name
    )
    mail.send(message)

