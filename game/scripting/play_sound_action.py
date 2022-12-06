from constants import *
from game.scripting.action import Action
from game.elements.sound import Sound


class PlaySoundAction(Action):

    def __init__(self, audio_service, filename):
        self._audio_service = audio_service
        self._filename = filename
        
    def execute(self, cast, script, callback):
        self._audio_service.stop_sound()
        sound = Sound(self._filename)
        self._audio_service.play_sound(sound)
        script.remove_action(OUTPUT, self)