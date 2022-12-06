from game.elements.text import Text


class Entity:
    """A thing that participates in the game."""
    
    def __init__(self, debug = False):
        """Constructs a new entity using the given group and id.
        
        Args:
            group: A string containing the entity's group name.
            id: A number that uniquely identifies the entity within the group.
        """
        self._idx = 0
        self._debug = debug
        
    def is_debug(self):
        """Whether or not the entity is being debugged.
        
        Returns:
            True if the entity is being debugged; False if otherwise.
        """
        return self._debug
    
    def set_idx(self, idx):
        self._idx = idx
    
    def get_idx(self):
        return self._idx