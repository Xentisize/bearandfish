import collections
import random
import itertools
import draw_grid

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

grids_x = 5
grids_y = 5

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
    if x >= 0 and y >= 0:
        return x < grids_x and y < grids_y
    return False


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
        self._died = False
        grids[self._position] = self

    @property
    def position(self):
        return self._position

    def _is_same_species(self, x, y):
        creature_at_grid = grids[Coordinate(x, y)]
        return isinstance(creature_at_grid, self.__class__)

    def _move_to_new_coordinate(self, x, y):
        # print("Inside Creature _move_to_new_coordinate")
        # print(f'{self} in {self.position} is moving to {Coordinate(x, y)}\n')
        global grids
        # print(f'\nPrinting full grids before: {grids}.\n')
        grids[self.position] = None
        # print(f"Original grids is: {# grids[self.position]}.")
        self._position = Coordinate(x, y)
        # print(f'{self}\'s new postion: {# self.position}.')
        grids[self.position] = self
        # print(f'\nPrinting full grids before: {grids}.\n')

        # print(f'{self}\'s new position in {grids[self.position]}.')


    def _out_of_boundary(self, x, y):
        return f'{self} cannot move to {Coordinate(x, y)}. Out of Boundary.\n'


    def move(self):
        global grids
        new_x, new_y = get_direction(self._position.x, self._position.y)
        # print(f'The new direction for {self} is {Coordinate(new_x, new_y)}.')
        if in_boundary(new_x, new_y) and not is_occupied(new_x, new_y):
            self._move_to_new_coordinate(new_x, new_y)
        elif not in_boundary(new_x, new_y):
            self._out_of_boundary(new_x, new_y)
        elif is_occupied(new_x, new_y):
            self.birth()

    def birth(self):
        x, y = random_coordinate(grids_x, grids_y)
        if Coordinate(x, y) not in all_occupied_cells():
            self.__class__()
            # print(f'New {new_creature} is at {new_creature.position}.')


class Fish(Creature):

    _fish_id = itertools.count()

    def __init__(self):
        super().__init__()
        self._id = next(self.__class__._fish_id)
        self._died = False
        # print(f'Fish {self._id} is born at {self.position}.')

    def move(self):
        new_x, new_y = get_direction(self._position.x, self._position.y)
        # print(f'{self}\'s new direction is {Coordinate(new_x, new_y)}.\n')
        if in_boundary(new_x, new_y) and not is_occupied(new_x, new_y):
            self._move_to_new_coordinate(new_x, new_y)
        elif not in_boundary(new_x, new_y):
            self._out_of_boundary(new_x, new_y)
        elif is_occupied(new_x, new_y):
            if self._is_same_species(new_x, new_y):
                self.birth()
                # print(f'{self} mated with {grids[Coordinate(new_x, new_y)]}.')

    def __repr__(self):
        return f'Fish {self._id}'


class Bear(Creature):

    _bear_id = itertools.count()

    def __init__(self):
        super().__init__()
        self._id = next(self.__class__._bear_id)
        # print(f'Bear {self._id} is born at {self.position}.')
        self._eaten = []

    def __repr__(self):
        return f'Bear {self._id}'

    def move(self):
        new_x, new_y = get_direction(self._position.x, self._position.y)
        # print(f'{self}\'s new direction is {Coordinate(new_x, new_y)}.\n')
        if in_boundary(new_x, new_y) and not is_occupied(new_x, new_y):
            self._move_to_new_coordinate(new_x, new_y)
        elif not in_boundary(new_x, new_y):
            self._out_of_boundary(new_x, new_y)
        elif is_occupied(new_x, new_y):
            if self._is_same_species(new_x, new_y):
                self.birth()
                # print(f'{self} mated with {grids[Coordinate(new_x, new_y)]}.')
            else:
                prey = self.eat(grids[Coordinate(new_x, new_y)])
                return prey

    def eat(self, prey):
        self._eaten.append(str(prey))

        for k, v in grids.items():
            if v == prey:
                grids[k] = None
                break
        # print(f'{prey} was eaten by {self}.')
        return prey


if __name__ == '__main__':
    print("Starting to initialize animals.")
    for i in range(5):
        random_i = random.randint(0, 100)
        if random_i % 2 == 0:
            Fish()
        else:
            Bear()

    occupied = all_occupied_cells()
    occupied_in_words = [f'{grids[c]} in {c}' for c in occupied]

    round = 1

    while True:
        if len(occupied) == len(grids):
            break
        if round == 1000:
            break
        print("*" * 40)

        print(f'Round {round}')
        # print(f'All Occupied: {occupied}.')
        # print(f'Occupant: {sorted(occupied_in_words)}.\n')
        draw_grid.draw_grids(grids, grids_x, grids_y)
        for c in occupied:
            if grids[c] is None:
                continue
            if not grids[c]._died:
                # print(f"Grid {c}: {grids[c]}.")
                grids[c].move()
            else:
                del grids[c]
        occupied = all_occupied_cells()
        occupied_in_words = [f'{grids[c]} in {c}' for c in occupied]
        round += 1

    print("Simulation ended.")
    bears = [grids[b] for b in occupied if isinstance(grids[b], Bear)]
    for b in bears:

        print(f'{b} has eatern {b._eaten}.')





