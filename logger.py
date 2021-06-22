import logging
from logging.handlers import RotatingFileHandler


def get_logger():
    log_path = 'err.log'
    logger = logging.getLogger("Error Log")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        log_path, maxBytes=10000, backupCount=5
    )
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

