import os


class Config:
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('KINYOZI_DB')  # "sqlite:///app.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_ADDRESS')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
