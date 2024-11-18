import logzero
from logzero import logger

class LogService:

    @staticmethod
    def log_info(message):
        log_format = '[INFO %(asctime)s] %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        formatter = logzero.LogFormatter(fmt=log_format, datefmt=date_format)
        logzero.setup_default_logger(level='INFO', formatter=formatter)
        logger.info(message)

    @staticmethod
    def log_error(message):
        log_format = '[ERROR %(asctime)s] %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        formatter = logzero.LogFormatter(fmt=log_format, datefmt=date_format)
        logzero.setup_default_logger(level='ERROR', formatter=formatter)
        logger.error(message)
