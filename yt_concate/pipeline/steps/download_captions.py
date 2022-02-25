import time
import concurrent.futures
import logging

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            for yt in data:
                if inputs['fast']:
                    if utils.caption_file_exists(yt):
                        logger.info(f'found downloaded caption files: {yt.id}')
                        continue

                executor.submit(self.download_captions, yt)

        end = time.time()
        logger.info(f'took {end - start} seconds')
        return data

    def download_captions(self, yt):
        logger = logging.getLogger('yt_concate.log.' + __name__)
        try:
            source = YouTube(yt.url)
            caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = caption.generate_srt_captions()
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            logger.info(f'successfully downloaded captions for : {yt.url}')

        except (KeyError, AttributeError):
            logger.info(f'An error when downloading captions for : {yt.url}')




