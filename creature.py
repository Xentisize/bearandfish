from river import Coordinate

class Creature:
    """Creature is the base class for implementing Bear and Fish"""
    def __init__(self, name, _id, location=(0, 0)):
        self._id = _id
        self._name = name
        self._position = Coordinate(*location)

    def move(self, x, y):
        x = self.position.x + x
        y = self.position.y + y
        self._position = Coordinate(x, y)

    @property
    def position(self):
        return self._position



