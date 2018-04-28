import collections
import random

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

class River:

    def __init__(self, x, y):
        self._grids = {Coordinate(x, y): [None, False] for i in range(x) for j in range(y)}
        self._x_dimension = x
        self._y_dimension = y

    def _isoccupied(self, x, y):
        return self._grids[Coordinate(x, y)[0]]


    def _occupy(self, creature, x, y):
        self._grids[Coordinate(x, y)] = creature

    def _find_feasible_grid(self):
        while True:
            proposed_x = random.randint(self._x_dimension)
            proposed_y = random.randint(self._y_dimension)
            if not self._isoccupied(proposed_x, proposed_y):
                return (proposed_x, proposed_y)






