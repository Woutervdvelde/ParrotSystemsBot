import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")
DEFAULT_TEXT_MODEL = os.getenv("DEFAULT_TEXT_MODEL", "tts_models/nl/css10/vits")
DEFAULT_AUDIO_FOLDER = os.getenv("DEFAULT_AUDIO_FOLDER", "audio")