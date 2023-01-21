import os
import re
from CoquiTTS.api import TTS as CoquiTTS
from config import DEFAULT_TEXT_MODEL, DEFAULT_AUDIO_FOLDER
from functools import cache

class TTS:
    def __init__(self, model_name= DEFAULT_TEXT_MODEL):
        self.model_name = model_name
        self.model = TTS.get_tts_model(self.model_name)

    @staticmethod
    @cache
    def get_tts_model(model_name):
        return CoquiTTS(model_name)

    def synthesize(self, text):
        filename = re.sub(r'\W+', '', text)
        filepath = f'{DEFAULT_AUDIO_FOLDER}/{filename}.wav'
        self.model.tts_to_file(text=text, file_path=filepath)
        return filepath

    def delete_audio(self, filepath):
        os.remove(filepath)
