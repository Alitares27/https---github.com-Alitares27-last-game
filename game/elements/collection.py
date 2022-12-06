class Collection:
    """A collection of entities."""

    def __init__(self):
        """Constructs a new entity."""
        self._entities = {}
        
    def add_entity(self, group, entity):
        """Adds an entity to the given group.
        
        Args:
            group: A string containing the name of the group.
            entity: The instance of entity (or a subclass) to add.
        """
        if group not in self._entities.keys():
            self._entities[group] = []
        self._entities[group].append(entity)

    def clear_entities(self, group):
        """Clears entities from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._entities:
            self._entities[group] = []
    
    def clear_all_entities(self):
        """Clears all entities."""
        for group in self._entities:
            self._entities[group] = []
    
    def get_entities(self, group):
        """Gets the entities in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of entity instances.
        """
        results = []
        if group in self._entities.keys():
            results = self._entities[group].copy()
        return results
    
    def get_all_entities(self):
        """Gets all of the entities in the collection.
        
        Returns:
            A list of entity instances.
        """
        results = []
        for group in self._entities:
            results.extend(self._entities[group])
        return results

    def get_first_entity(self, group):
        """Gets the first entity in the given group.
        
        Args:
            group: A string containing the name of the group.
            
        Returns:
            An instance of entity.
        """
        result = None
        if group in self._entities.keys():
            result = self._entities[group][0]
        return result
    
    def get_entity_by_idx(self, group, idx):
        """Gets the first entity in the given group.
        
        Args:
            group: A string containing the name of the group.
            
        Returns:
            An instance of entity.
        """
        result = None
        if group in self._entities.keys():
            result = self._entities[group][idx]
        return result

    def remove_entity(self, group, entity):
        """Removes an entity from the given group.
        
        Args:
            group: A string containing the name of the group.
            entity: The instance of entity (or a subclass) to remove.
        """
        if group in self._entities:
            self._entities[group].remove(entity)