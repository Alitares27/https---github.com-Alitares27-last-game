import csv
from constants import *
from game.elements.animation import Animation
from game.elements.ball import Ball
from game.elements.body import Body
from game.elements.image import Image
from game.elements.label import Label
from game.elements.point import Point
from game.elements.racket import Racket
from game.elements.stats import Stats
from game.elements.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.collide_border_action import CollideBordersAction
from game.scripting.collide_racket_action import CollideRacketAction
from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetssAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the collection and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_RACKET_ACTION = MoveRacketAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetssAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, collection, script):
        if scene == NEW_GAME:
            self._prepare_new_game(collection, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(collection, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(collection, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(collection, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(collection, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, collection, script):
        self._add_stats(collection)
        self._add_scores(collection)
        self._add_ball(collection)
        self._add_rackets(collection)
        self._add_dialog(collection, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, INIT_SOUND))
        
    def _prepare_next_level(self, collection, script):
        self._add_ball(collection)
        self._add_rackets(collection)
        self._add_dialog(collection, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, collection, script):
        self._add_ball(collection)
        self._add_rackets(collection)
        self._add_dialog(collection, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, collection, script):
        self._activate_ball(collection)
        collection.clear_entities(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, collection, script):
        self._add_ball(collection)
        self._add_rackets(collection)
        self._add_dialog(collection, WAS_GOOD_GAME)
        winner = ""
        for stat in collection.get_entities(STATS_GROUP):
            if stat.get_is_winner():
                winner = stat.get_name()
        self._add_dialog_winner(collection, winner)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # elements methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, collection):
        ball = collection.get_first_entity(BALL_GROUP)
        ball.release()

    def _add_ball(self, collection):
        collection.clear_entities(BALL_GROUP)
        x = CENTER_X - BALL_WIDTH / 2
        y = CENTER_Y - BALL_HEIGHT
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        collection.add_entity(BALL_GROUP, ball)

    def _add_dialog(self, collection, message):
        collection.clear_entities(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        collection.add_entity(DIALOG_GROUP, label)
    
    def _add_dialog_winner(self, collection, winner):
        message = WINNER_GAME.format(winner)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y + FRAME_RATE)
        label = Label(text, position)
        collection.add_entity(DIALOG_GROUP, label)

    def _add_scores(self, collection):
        collection.clear_entities(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        label = Label(text, SCORE_A_POSITION)
        collection.add_entity(SCORE_GROUP, label)
        
        label_b = Label(text, SCORE_B_POSITION)
        collection.add_entity(SCORE_GROUP, label_b)

    def _add_stats(self, collection):
        collection.clear_entities(STATS_GROUP)
        stat = Stats()
        stat.set_name(PLAYER_A_NAME)
        collection.add_entity(STATS_GROUP, stat)
        
        stat_b = Stats()
        stat_b.set_name(PLAYER_B_NAME)
        collection.add_entity(STATS_GROUP, stat_b)

    def _add_rackets(self, collection):
        collection.clear_entities(RACKET_GROUP)
        x = (CENTER_X / 2) - (RACKET_WIDTH / 2)
        y = CENTER_Y - RACKET_HEIGHT/2
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        racket = Racket(body, animation)
        collection.add_entity(RACKET_GROUP, racket)
        
        position_b = Point(CENTER_X + x, y)
        body_b = Body(position_b, size, velocity)
        racket_b = Racket(body_b, animation)
        collection.add_entity(RACKET_GROUP, racket_b)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)