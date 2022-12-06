from constants import *
from game.elements.entity import Entity


class Stats(Entity):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._score = 0
        self._is_winner = False
        self._name = ""

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._score = 0
        self._is_winner = False
    
    def get_is_winner(self):
        return self._is_winner
    
    def set_is_winner(self, is_winner):
        self._is_winner = is_winner
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name