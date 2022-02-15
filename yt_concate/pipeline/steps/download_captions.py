import time
import concurrent.futures

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()

        for yt in data:
            if inputs['fast']:
                if utils.caption_file_exists(yt):
                    print('found downloaded caption files:', yt.id)
                    continue
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                executor.submit(self.download_captions, yt)

        end = time.time()
        print('took', end - start, 'seconds')
        return data

    def download_captions(self, yt):
        try:
            source = YouTube(yt.url)
            caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = caption.generate_srt_captions()
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            print('successfully downloaded:', yt.url)

        except (KeyError, AttributeError):
            print("An error when downloading captions for :", yt.url)




