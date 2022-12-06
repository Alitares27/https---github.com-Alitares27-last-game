# from curses.textpad import rectangle
# from email.mime import image
# from turtle import position
from constants import *
from game.scripting.action import Action

class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, collection, script, callback):
        rackets = collection.get_entities(RACKET_GROUP)
        
        for racket in rackets:
            body = racket.get_body()

            animation = racket.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)


    