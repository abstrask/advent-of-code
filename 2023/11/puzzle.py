#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import numpy as np
import collections
import itertools


def calc_a(input):
    result = None
    return result

def get_galaxies(input: str):
    # Convert multi-line string to regular array, then NP array
    ary = []
    for line in input.splitlines():
        ary.append(list(line))
    a = np.array(ary)
    # print()
    # print(a)

    # Expand empty space
    # print()
    ro = 0 # row offset
    (rows, cols) = a.shape
    for i in range(rows):
        row = i + ro
        # print(f'{i=} {row=}')
        # print(a[row])
        c = collections.Counter(a[row])
        if '.' in c and len(c) == 1: # empty space?
            a = np.insert(a, row, ".", axis=0)
            ro += 1
    co = 0 # column offset
    for i in range(cols):
        col = i + co
        # print(f'{c=} {col=}')
        # print(a[:, col])
        c = collections.Counter(a[:, col])
        if '.' in c and len(c) == 1: # empty space?
            a = np.insert(a, col, ".", axis=1)
            co += 1

    # Spot galaxies
    # print()
    gal = {}
    (rows, cols) = a.shape
    # print(f'{rows=} {cols=}')
    for r in range(rows):
        for c in range(cols):
            # print(f'{r=} {c=}')
            if a[r, c] == '#':
                gal_no = len(gal)+1
                gal[gal_no] = (r, c)
    # print(f'{gal=}')
    return gal


def solve_a(input):
    dist = 0
    gal = get_galaxies(input)
    combo = itertools.combinations(gal.keys(), 2)

    # print(f'{gal=}')
    for c in combo:
        x = [gal[g][0] for g in c] # galaxies' x-coordinates
        y = [gal[g][1] for g in c] # galaxies' y-coordinates
        d = max(x) - min(x) + max(y) - min(y) # distance is the difference between x and y coordinates, respectively
        dist += d
        # print(f'{c=} {x=} {y=} {d=}')
    return dist


def calc_b(input):
    result = None
    return result


def solve_b(input):
    result = 0
    for line in input.split('\n'):
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
