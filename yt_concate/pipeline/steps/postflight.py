from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
        channel_id = inputs['channel_id']
        search_word = inputs['search_word']

        if inputs['clean_up']:
            if utils.output_file_exists(channel_id, search_word):
                utils.delete_downloaded_files(channel_id)
                print('all files produced by this project have been deleted')





