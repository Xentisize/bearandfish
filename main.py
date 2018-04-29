import collections
import random
import itertools

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

grids_x = 10
grids_y= 10

grids = {Coordinate(x,y): None for x in range(grids_x) for y in range(grids_y)}


def is_occupied(x, y):
    if in_boundary(x, y):
        return bool(grids[Coordinate(x, y)])
    else:
        return False


def random_coordinate(x, y):
    x = random.randint(0, x-1)
    y = random.randint(0, y-1)
    return x, y


def all_occupied_cells():
    return [cell for cell in grids.keys() if grids[cell]]


directions = [0, 3, 6, 9]


def get_direction(x, y):
    """
    0-3-6-9 represents the N-E-S-W
    :param integer: random integer for movement
    :param x: current x-coord
    :param y: current y-coord
    :return: the intended x, y-coord for movement
    """
    direction = random.choice(directions)

    if direction == 0:
        return x, y + 1
    elif direction == 3:
        return x + 1, y
    elif direction == 6:
        return x, y - 1
    elif direction == 9:
        return x - 1, y


def in_boundary(x, y):
    return x < grids_x and y < grids_y and x >= 0 and y >= 0


class Creature:
    """
    The base class for Bear and Fish.

    Args:
        x: The horizontal position of the creature.
        y: The vertical position of the creature.

    Attributes:
        position(Coordinate): the position of the creature.

    """
    # _creature_id = itertools.count()

    def __init__(self):
        # x, y = random_coordinate(grids_x, grids_y)
        # self._position = Coordinate(x, y)
        while True:
            x, y = random_coordinate(grids_x, grids_y)
            if not is_occupied(x, y):
                self._position = Coordinate(x, y)
                break
            # print(f'Initializing of {self} failed.')
        # self._position = Coordinate(x, y)
        grids[self._position] = self

    @property
    def position(self):
        return self._position

    def move(self):
        """
        :param x: The final x-coordinate of the creature.
        :param y: The final y-coordinate of the creature.
        :return: None

        Should check if the grid movable before moving actually.
        """
        new_x, new_y = get_direction(self._position.x, self._position.y)
        if in_boundary(new_x, new_y) and not is_occupied(new_x, new_y):
            print(f'{self} in {self._position} is moving to {Coordinate(new_x, new_y)}\n')
            grids[self._position] = None
            self._position = Coordinate(new_x, new_y)
            grids[self._position] = self
            return self
        elif not in_boundary(new_x, new_y):
            print(f'{self} cannot escape to {Coordinate(new_x, new_y)}.\n')
        elif is_occupied(new_x, new_y):
            print(f'{Coordinate(new_x, new_y)} is occupied.\nI will give a birth.')
            self.__class__()
            print(f'({self}) is crashing at Coordinate({new_x}, {new_y}).\nBecause it is out of boundary or someone is in it.')

    def birth(self):
        x, y = random_coordinate(grids_x, grids_y)
        if Coordinate(x, y) not in all_occupied_cells():
            new_creature = self.__class__(x, y)
            print(f'New {new_creature} is at {new_creature.position}.')


class Fish(Creature):

    _fish_id = itertools.count()

    def __init__(self):
        super().__init__()
        self._id = next(self.__class__._fish_id)

    def __repr__(self):
        return f'Fish {self._id}'


class Bear(Creature):

    _bear_id = itertools.count()

    def __init__(self):
        super().__init__()
        self._id = next(self.__class__._bear_id)
        self._eaten = []

    def __repr__(self):
        return f'Bear {self._id}'

    def eat(self, prey):
        if isinstance(prey, Fish):
            self._eaten.append(str(prey))

            for k, v in grids.items():
                if v == prey:
                    del grids[k]
                    break

            print(f'{prey} was eaten by {self}.')
            del prey






if __name__ == '__main__':
    for i in range(5):
        random_i = random.randint(0, 100)
        if random_i % 2 == 0:
            Fish()
            print(f'New Fish is born.')
        else:
            Bear()
            print(f'New Bear is born.')

    occupied = [c for c in grids.keys() if grids[c]]


    print(f'All Grids: {grids}.\n\n')

    for i in range(5):
        print("*" * 40)
        print(f'Round {i}')
        occupied = all_occupied_cells()
        print(f'All Occupied: {occupied}.\n\n')
        for c in occupied:
            print(f"Grid {c}: {grids[c]}.")
            # print('')
            grids[c].move()

    # occupied = all_occupied_cells()
    # print(occupied)
    #
    # for c in occupied:
    #     x, y = random_coordinate(grids_x, grids_y)
    #     # print(f'The random coordinate is: {x}, {y}.')
    #     grids[c].move(x, y)
    #
    # print(all_occupied_cells())


