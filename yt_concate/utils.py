import os
import shutil
import sys
import logging

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import OUTPUTS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        filepath = self.get_video_list_filepath(channel_id)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def caption_file_exists(self, yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exists(self, yt):
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_output_filepath(self, channel_id, search_word):
        filename = f'{channel_id}_{search_word}.mp4'
        return os.path.join(OUTPUTS_DIR, filename)

    def output_file_exists(self, channel_id, search_word):
        filepath = self.get_output_filepath(channel_id, search_word)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def output_file_replacement_check(self, channel_id, search_word):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        if self.output_file_exists(channel_id, search_word):
            a = input('output file has already existed, still want to proceed ? (Y/N) ')

            if a == 'Y' or a == 'y':
                logger.info('processing')

            elif a == 'N' or a == 'n':
                logger.info('stop running')
                sys.exit(0)

    def delete_downloaded_files(self, channel_id):
        shutil.rmtree(DOWNLOADS_DIR)
        shutil.rmtree(OUTPUTS_DIR)
        os.remove(self.get_video_list_filepath(channel_id))













