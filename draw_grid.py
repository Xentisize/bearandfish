from main import Coordinate, Fish, Bear

def draw_horizontal_line(length=9):
    print('****' * length + '*')


def draw_all_cells(length=9):
    print('*   ' * length + '*')


def draw_single_empty_cell():
    print('*   ', end='')


def draw_empty_grid(length, width):
    for w in range(width):
        draw_horizontal_line(length)
        draw_all_cells(length)
    draw_horizontal_line(length)


def bear_or_fish(animal):
    if animal.__class__.__name__ == 'Fish':     # Because I can't make a cross-package instanceof() check
        return 'F'
    else:
        return 'B'


def draw_grids(grids, x, y):
    length = x
    width = y

    draw_horizontal_line(x)

    for l in range(length):
        for w in range(width):
            cell = grids[Coordinate(l, w)]
            if cell:
                animal = bear_or_fish(cell)
                print(f'* {animal} ', end='')
            else:
                draw_single_empty_cell()
        print('*')
        draw_horizontal_line(length)
    print()

