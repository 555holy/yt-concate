import logging


def config_logger(level):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
    file_handler = logging.FileHandler('yt_concate.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

