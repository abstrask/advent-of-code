#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import numpy as np


def get_array(input):
    a = []
    for line in input.splitlines():
        a.append(list(line))
    a = np.array(a)
    r, c = np.where(a == 'S')
    return a, (r[0], c[0])


def solve_a(input):
    (a, s) = get_array(input)
    print()
    print(a)

    compass = {
        'N': (-1,  0), # north
        'S': ( 1,  0), # south
        'E': ( 0,  1), # east
        'W': ( 0, -1)  # west
    }

    pipes = {
        '|': (compass['N'], compass['S']),
        '-': (compass['E'], compass['W']),
        'L': (compass['N'], compass['E']),
        'J': (compass['N'], compass['W']),
        '7': (compass['S'], compass['W']),
        'F': (compass['S'], compass['E'])
    }

    pn = [tuple(np.add(s, (r, c))) for r, c in compass.values()] # potential neighbours
    sn = [(r, c) for r, c in pn if all(np.less((r,c), a.shape)) and all(np.greater_equal((r,c), (0,0)))] # valid neighbours (within bounds of array)

    loop = [s]

    # Find first connected pipe - this could probably be writte more elegantly, or combined with the logic below
    next = None
    for n in sn:
        if len(loop) > 1: # Next hop has been determined
            break
        p = a[n] # pipe
        if not p in pipes.keys():
            continue
        conn = [tuple(np.add(n, (r, c))) for r, c in pipes[p]]
        # print(f'{s=} {n=} {p=} {conn=}')
        for c in conn:
            if c == s:
                loop.append(n)
                break

    while True:
        l = loop[-1] # last coord
        p = a[l]     # pipe at last coord
        c = [tuple(np.add(l, (r, c))) for r, c in pipes[p]] # connections of last pipe
        u = loop[-2] # used conn
        n = [e for e in c if e != u][0] # unused conn: next coord
        if n == s: # back to beginning: loop complete
            break
        # print(f'{l=} {p=} {c=} {u=} {n=}')
        loop.append(n)

    # print(loop)
    # print(len(loop))
    result = int(len(loop) / 2)
    return result


def calc_b(input):
    result = None
    return result


def solve_b(input):
    result = 0
    for line in input.splitlines():
        result += calc_b(line)
    return result


def main():
    day = get_day_and_year()[0]
    year = get_day_and_year()[1]
    p = Puzzle(day=day, year=year)

    result_a = solve_a(data)
    print(f'Answer A: {result_a}')
    if not p.answered_a:
        p.answer_a = result_a

    if p.answered_a:
        result_b = solve_b(data)
        print(f'Answer B: {result_b}')
        if not p.answered_b:
            p.answer_b = result_b


if __name__ == '__main__':
    main()
