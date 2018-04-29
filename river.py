import collections
import random

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

class River:

    def __init__(self, x, y):
        """
        :param x: x-dimension of the whole grid
        :param y: y-dimension of the whole grid

        _grids[Coordinate(x, y)] = Creature
        """
        self._grids = {Coordinate(x, y): None for i in range(x) for j in range(y)}
        self._x_dimension = x
        self._y_dimension = y

    def _isoccupied(self, x, y):
        """Check if the Coordinate(x, y) has already been occupied."""
        return self._grids[Coordinate(x, y)]

    def _occupy(self, creature, x, y):
        self._grids[Coordinate(x, y)] = creature

    def _find_feasible_grid(self):
        while True:
            proposed_x = random.randint(self._x_dimension)
            proposed_y = random.randint(self._y_dimension)
            if not self._isoccupied(proposed_x, proposed_y):
                return (proposed_x, proposed_y)

    def main(self):
        """This is the mainloop for the simulation which will be terminated after all grids are occupied."""
        fully_occupied = False

        # while not fully_occupied:
        #     occupied_grid = []    # if all occupied cells have been scanned at first, it doesn't need "Waiting|Moved"?
        #     for k in self._grids.keys():
        #         if not self._grids[k][0]:
        #             self._grids[k][1] = 'Waiting'
        #             occupied_grid.append(k)
        #     for k in occupied_grid:

        while not fully_occupied:
            occupied_cells = [k for k in self._grids.keys() if self._grids[k]]

            for cell in occupied_cells:
                moving_direction = random.randint(0, 3)
                if moving_direction == 0 and cell.x + moving_direction <= self._x_dimension - 1:
                    if not self._isoccupied(cell.x + 1, y):
                        self._grids[Coordinate(cell.x + 1, y)] = self._grid[Coordinate(cell.x, y)]  # move the creature to the new grid
                        self._grid[Coordinate(cell.x, y)] = None    # unreference the original grid








