from turtle import position
from constants import *
from game.scripting.action import Action

class MoveBallAction(Action):

    def __init__(self):
        pass

    def execute(self, collection, script, callback):
        ball = collection.get_first_entity(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)