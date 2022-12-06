from constants import *
from game.scripting.action import Action

class DrawDialogAction(Action):

    def __init__(self, video_service):
        self._video_service =  video_service

    def execute(self, collection, script, callback):
        dialogs = collection.get_entities(DIALOG_GROUP)
        for dialog in dialogs:
            text = dialog.get_text()
            position = dialog.get_position()
            self._video_service.draw_text(text, position)