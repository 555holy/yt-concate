import logging

from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        logger.info('in Postflight')
        channel_id = inputs['channel_id']
        search_word = inputs['search_word']

        if inputs['clean_up']:
            utils.delete_downloaded_files(channel_id)
            logger.info('all files produced by this project have been deleted')





