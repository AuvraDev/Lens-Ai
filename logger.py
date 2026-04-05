import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='app.log'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)