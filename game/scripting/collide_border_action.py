from constants import *
from game.elements.sound import Sound
from game.scripting.action import Action

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, collection, script, callback):
        ball = collection.get_first_entity(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        if x < (FIELD_LEFT + BALL_WIDTH):
            # opposite score to add points
            stat_b = collection.get_entity_by_idx(STATS_GROUP, PLAYER_B_IDX)
            stat_b.add_points(PLAYER_DEFAULT_POINTS)
            if stat_b.get_score() >= GAME_MAX_SCORE:
                stat_b.set_is_winner(True)
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)
            else:
                callback.on_next(TRY_AGAIN)
        
        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            stat_a = collection.get_entity_by_idx(STATS_GROUP, PLAYER_A_IDX)
            stat_a.add_points(PLAYER_DEFAULT_POINTS)
            if stat_a.get_score() >= GAME_MAX_SCORE:
                stat_a.set_is_winner(True)
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)
            else:
                callback.on_next(TRY_AGAIN)

        if y < (FIELD_TOP + (BALL_HEIGHT/2)):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - (BALL_HEIGHT/2)):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
            