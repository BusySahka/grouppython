from logtail import LogtailHandler
import logging

SOURCE_TOKEN = 'nvKyNdxY6tKXzfmMuaPcLKC6'
HOST = 's1516023.eu-nbg-2.betterstackdata.com'

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []

    logtail_handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger.addHandler(logtail_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    return logger

logger = get_logger()

logger.info("some info log", extra={"user_id": 23556})
logger.error("some error log")
