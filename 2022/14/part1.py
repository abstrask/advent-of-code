import os
from itertools import pairwise


def init_grid():
    global grid
    grid = []
    for y in range(0, bounds['y_high']+1):
        grid.append(['.']*(bounds['x_high']-bounds['x_low']+1))
    return


def populate_rocks():
    for cmdline in commands:
        for coord_a, coord_b in pairwise(cmdline):
            from_x = min([coord_a[0], coord_b[0]]) - bounds['x_low']
            from_y = min([coord_a[1], coord_b[1]])
            to_x = max([coord_a[0], coord_b[0]]) - bounds['x_low']
            to_y = max([coord_a[1], coord_b[1]])
            for y in range(from_y, to_y+1):
                for x in range(from_x, to_x+1):
                    # print(f"x: {x}, y: {y}")
                    grid[y][x] = '#'
    return


def init(input):
    global commands
    commands = []
    global bounds
    bounds = {}
    for line in input.splitlines():
        cmdline = []
        for coord in line.split(' -> '):
            x, y = [int(i) for i in coord.split(',')]

            # Only need low? Just set x_offset?
            if 'x_low' in bounds:
                if x < bounds['x_low']:
                    bounds['x_low'] = x
            else:
                bounds['x_low'] = x

            if 'x_high' in bounds:
                if x > bounds['x_high']:
                    bounds['x_high'] = x
            else:
                bounds['x_high'] = y

            if 'y_high' in bounds:
                if y > bounds['y_high']:
                    bounds['y_high'] = y
            else:
                bounds['y_high'] = y

            cmdline.append([x, y])
        commands.append(cmdline)
    # print(commands)
    # print(bounds)
    init_grid()
    populate_rocks()
    print_grid()
    return


def print_grid():
    # os.system('clear')
    for line in grid:
        print(''.join(line))
    return


def main():
    with open('input.txt') as f:
        input = f.read()
        print(init(input))


if __name__ == '__main__':
    main()
