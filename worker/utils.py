import os
import logging

def _setup_logging(logger):
    log_level = str(os.getenv('LOG_LEVEL', 'INFO')).upper()
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
