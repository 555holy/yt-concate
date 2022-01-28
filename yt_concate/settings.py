import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'download'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')