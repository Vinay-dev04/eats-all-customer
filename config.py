import os
import logging
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
db = SQLAlchemy()
class Config:
    try:
        # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:Admin123@192.168.31.200/jr_eats_db'
        SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:Srikar123@localhost/jreats_db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        logger.info("Database configuration set successfully")
    except Exception as e:
        logger.error("Error in Config setup for Database: %s", e)

    try:
        MAIL_SERVER = ''
        MAIL_PORT = 0
        MAIL_USERNAME = ''
        MAIL_PASSWORD = '' 
        MAIL_USE_TLS = False
        MAIL_USE_SSL = False
        MAIL_DEFAULT_SENDER = ''
        logger.info("Mail configuration set successfully")
    except Exception as e:
        logger.error("Error in Config setup for Mail details: %s", e)

    try :
        API_KEY = ""
        OTP_API_URL = '' 
        logger.info("OTP configuration set successfully")

    except Exception as e:
        logger.error("Error in Config setup for OTP details: %s", e)
    try:
        RAZORPAY_KEY_ID=''
        RAZORPAY_KEY_SECRET=''
        logger.info("Payment configuration set successfully")
    except Exception as e:
        logger.error("Error in Config setup for Payment details: %s", e)
    
    try:
        SECRET_KEY = ''  # This is for sessions and tokens
        JWT_SECRET_KEY = ''  # JWT secret
        JWT_ACCESS_TOKEN_EXPIRES = 900
        JWT_REFRESH_TOKEN_EXPIRES=2592000
        logger.info("JWT and Security configuration set successfully")
    except Exception as e:
        logger.error("Error in Config setup for JWT and Security details: %s", e)