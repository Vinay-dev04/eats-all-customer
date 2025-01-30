import logging
from logging.handlers import RotatingFileHandler
# from app import app


def setup_logging(app):
    handler = RotatingFileHandler('/home/applogs/customer.log', 
                                  maxBytes=10 * 1024 * 1024, backupCount=5)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logging.getLogger('__name__').setLevel(logging.INFO)  # For Flask request logs
    app.logger.addHandler(handler)
    app.logger.info("Logging is configured.")



    

