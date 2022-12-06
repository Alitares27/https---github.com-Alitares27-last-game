from email.mime import audio
from game.scripting.action import Action

class UnloadAssetssAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, collection, script, callback):
        self._audio_service.unload_sounds()
        self._video_service.unload_fonts()
        self._video_service.unload_images()