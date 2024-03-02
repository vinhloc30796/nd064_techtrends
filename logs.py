import logging
from flask import request

class ContextualFilter(logging.Filter):
    def filter(self, log_record):
        log_record.ip = request.remote_addr if request else None
        return True

def init_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter("%(levelname)s:%(name)s:%(ip)s - - [%(asctime)s] %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(format)
    logger.addHandler(stream_handler)
    logger.addFilter(ContextualFilter())

    return logger