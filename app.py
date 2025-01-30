from flask import Flask
# from .models.__init__ import db
from controllers.customer_controller import customer_controller
from controllers.school_controller import school_controller
from controllers.pickup_controller import pickup_controller
from config import Config,db
from flask_cors import CORS
from logging_config import setup_logging
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from controllers.notifications_controller import notifications_bp
#from flask_swagger_ui import get_swaggerui_blueprint
#from flasgger import Swagger

# Determine the environment
env = os.getenv('FLASK_ENV')
# print(env)
# Load the appropriate .env file
if env == 'prd':
    load_dotenv('.env.prd')
elif env == 'stg':
    load_dotenv('.env.stg')
elif env == 'dev':
    load_dotenv('.env.dev')
elif env=='local':
    load_dotenv('.env.local')
else:
    print('Env Not Found')


app = Flask(__name__)
CORS(app)

#Swagger=Swagger(app)
#SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
#API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)
'''
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },)
app.register_blueprint(swaggerui_blueprint)
'''

# Now you can access your environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = os.getenv('DEBUG') == 'True'

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER') 

app.config['API_KEY'] = os.getenv('API_KEY')
app.config['OTP_API_URL'] = os.getenv('OTP_API_URL') 

app.config['RAZORPAY_KEY_ID']=os.getenv('RAZORPAY_KEY_ID')
app.config['RAZORPAY_KEY_SECRET']=os.getenv('RAZORPAY_KEY_SECRET')

app.config['SECRET_KEY']=os.getenv('SECRET_KEY')or'default_SECRET_KEY'
app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET_KEY')or'default_JWT_SECRET_KEY'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 2592000
# OTP_API_URL=os.getenv('OTP_API_URL') 
# Initialize databases
jwt = JWTManager(app)

db.init_app(app)
# school_db.init_app(app)

# Register Blueprints
app.register_blueprint(customer_controller, url_prefix='/')
app.register_blueprint(school_controller, url_prefix='/')
app.register_blueprint(notifications_bp, url_prefix='/')
app.register_blueprint(pickup_controller,url_prefix='/')
# Setup logging
# from logging_config import setup_logging
setup_logging(app)
# request_otp(OTP_API_URL)
mail = Mail(app)

if __name__ == '__main__':
    app.run( host="0.0.0.0", port=5000, debug=True)