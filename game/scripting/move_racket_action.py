from turtle import position
from constants import *
from game.elements.point import Point
from game.scripting.action import Action

class MoveRacketAction(Action):

    def __ini__(self):
        pass

    def execute(self, collection, script, callback):
        rackets = collection.get_entities(RACKET_GROUP)
        for racket in rackets:
            body = racket.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            y = position.get_y()

            position = position.add(velocity)

            if y < FIELD_TOP:
                position = Point(position.get_x(), FIELD_TOP)
            elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
                position = Point(position.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)

            body.set_position(position)