from turtle import position
from constants import *
from game.scripting.action import Action

class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, collection, script, callback):
        stats = collection.get_entities(STATS_GROUP)
        stat_count = 0
        for stat in stats:
            self._draw_label(collection, SCORE_GROUP, stat_count, SCORE_FORMAT, stat.get_score())
            stat_count+=1

    def _draw_label(self, collection, group, object_idx, format_str, data):
        the_value_to_display = format_str.format(data)
        label = collection.get_entity_by_idx(group, object_idx)
        text = label.get_text()
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)