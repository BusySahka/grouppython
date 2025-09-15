from logtail import LogtailHandler
import logging

SOURSE_TOKEN = 'nvKyNdxY6tKXzfmMuaPcLKC6'
HOST = 's1516023.eu-nbg-2.betterstackdata.com'


def get_logger():
    handler = LogtailHandler(
        source_token='$SOURCE_TOKEN',
        host=f'https://{HOST}',
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)
    return logger