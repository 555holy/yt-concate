import concurrent.futures
import time
import logging

import youtube_dl

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        count = 0
        start = time.time()
        yt_set = set([found.yt for found in data])
        logger.info(f'videos to download {len(yt_set)}')

        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            for yt in yt_set:
                count += 1
                url = yt.url
                if inputs['fast']:
                    if utils.video_file_exists(yt):
                        logger.info(f'found existing video file for {url}, skipping')
                        continue

                if count > inputs['limit']:
                    break
                executor.submit(self.download_videos, yt)

        end = time.time()
        logger.info(f'took {end-start} seconds')
        return data

    def download_videos(self, yt):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        logger.info('downloading')
        ydl_opts = {
            'format': 'best[height<=480]',
            'outtmpl': yt.video_filepath,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt.url])
        logger.info(f'successfully downloaded: {yt.url}')



