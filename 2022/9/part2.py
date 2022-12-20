import os
from sys import exit
from itertools import chain
from time import sleep


def main(input):
    global rope
    rope = {}
    global num_tails
    num_tails = 9
    for i in range(num_tails+1):
        rope[i] = [[0, 0]]
    for line in input.splitlines():
        direction, moves = line.split()
        move_head(direction, int(moves))
    # print_rope()
    tail_pos = []
    for pos in rope[num_tails]:
        tail_pos.append("%s,%s" % (pos[0], pos[1]))
    return len(set(tail_pos))


def sign(number: int):
    match number:
        case _ if number > 0:
            return 1
        case _ if number < 0:
            return -1
        case _ if number == 0:
            return 0


def move_head(direction: str, moves: int):
    last = rope[0][-1]
    x = last[0]
    y = last[1]
    for _ in range(moves):
        match direction:
            case 'U':
                y += 1
            case 'L':
                x -= 1
            case 'R':
                x += 1
            case 'D':
                y -= 1
            case _:
                exit(1)
        rope[0].append([x, y])
        move_tail()
    return


# Head and tails need to be in same ordered collection
# Each tail need to lookup position of index -1

def move_tail():
    for i in rope.keys():
        if i == 0:
            continue
        last = rope[i][-1]
        x = last[0]
        y = last[1]
        leader = rope[i-1][-1]  # last position of leader
        # print(f"i: {i}, last: {last}, leader: {leader}")
        x_diff = leader[0] - x
        y_diff = leader[1] - y
        # print(f"Tail: {x}, {y}")
        # print(f"Head: {x_head}, {y_head}")
        # print(f"Diff: {x_diff}, {y_diff}")
        if max([abs(x_diff), abs(y_diff)]) > 1:
            x += sign(x_diff)
            y += sign(y_diff)
        # print(f"New:  {x}, {y}")
        rope[i].append([x, y])
    return


def get_bounds():
    bounds = {}
    for v in rope.values():
        for coord in v:
            x, y = coord

            if 'x_low' in bounds:
                if x < bounds['x_low']:
                    bounds['x_low'] = x
            else:
                bounds['x_low'] = x

            if 'x_high' in bounds:
                if x > bounds['x_high']:
                    bounds['x_high'] = x
            else:
                bounds['x_high'] = x

            if 'y_low' in bounds:
                if y < bounds['y_low']:
                    bounds['y_low'] = y
            else:
                bounds['y_low'] = y

            if 'y_high' in bounds:
                if y > bounds['y_high']:
                    bounds['y_high'] = y
            else:
                bounds['y_high'] = y
    return bounds


def reset_grid(bounds):
    grid = []
    x_count = bounds['x_high']-bounds['x_low']+1
    y_count = bounds['y_high']-bounds['y_low']+1
    for _ in range(y_count):
        grid.append(['.']*x_count)
    grid[0 - bounds['y_low']][0 - bounds['x_low']] = 's'
    return grid


def print_rope():

    bounds = get_bounds()

    # Update grid with rope
    for i, _ in enumerate(rope[0]):

        grid = reset_grid(bounds)

        for k, item in sorted(rope.items(), reverse=True):
            if k == 0:
                c = 'H'
            else:
                c = str(k)
            x, y = item[i]  # last coord
            grid[y - bounds['y_low']][x - bounds['x_low']] = c

        sleep(0.1)

        # Print grid
        # os.system('clear')
        print()
        for line in reversed(grid):
            print(''.join(line))

    sleep(3)
    return


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(main(input))
