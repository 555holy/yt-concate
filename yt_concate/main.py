import sys
import getopt
import logging
from distutils.util import strtobool

# from yt_concate.log import config_logger
from yt_concate import log
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main(argv):

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    inputs = {
        'channel_id': 'UCKSVUHI9rbbkXhvAXK-2uxA',
        'search_word': 'incredible',
        'limit': 20,
        'output_file_replacement': True,
        'fast': True,
        'clean_up': False,
        'logging_level': logging.DEBUG,
    }

    short_opts = "hc:s:l:o:f:"
    long_opts = "channel_id= search_word= limit= output_file_replacement= fast= clean_up= logging_level= ".split()

    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)

    except getopt.GetoptError:
        print()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('python main -c <channel_id> -s <search_word> -l<limit>')
            sys.exit(0)
        elif opt in ("-c", "--channel_id"):
            inputs['channel_id'] = arg
        elif opt in ("-s", "--search_word"):
            inputs['search_word'] = arg
        elif opt in ("-l", "--limit"):
            inputs['limit'] = bool(strtobool(arg))
        elif opt in ("-o", "--output_file_replacement"):
            inputs['output_file_replacement'] = bool(strtobool(arg))
        elif opt in ("-f", "--fast"):
            inputs['fast'] = bool(strtobool(arg))
        elif opt in "--clean_up":
            inputs['clean_up'] = bool(strtobool(arg))
        elif opt in "--logging_level":
            inputs['logging_level'] = arg

    log.config_logger(inputs['logging_level'])
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main(sys.argv[1:])

