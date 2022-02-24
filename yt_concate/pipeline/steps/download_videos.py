import concurrent.futures
import time

from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        yt_set = set([found.yt for found in data])
        print('videos to download', len(yt_set))

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for yt in yt_set:
                url = yt.url
                if inputs['fast']:
                    if utils.video_file_exists(yt):
                        print(f'found existing video file for {url}, skipping')
                        continue
                executor.submit(self.download_videos, yt)

        end = time.time()
        print('took', end-start, 'seconds')
        return data

    def download_videos(self, yt):
        print('downloading')
        YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
        print('successfully downloaded:', yt.url)

