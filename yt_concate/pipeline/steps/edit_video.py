from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from .step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        channel_id = inputs['channel_id']
        search_word = inputs['search_word']

        if inputs['output_file_replacement']:
            utils.output_file_replacement_check(channel_id, search_word)

        for found in data:
            if not utils.video_file_exists(found.yt):
                continue

            if len(clips) > inputs['limit']:
                break

            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)


    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000






