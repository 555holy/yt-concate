import logging

from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        logger.info('in Preflight')
        utils.create_dirs()
