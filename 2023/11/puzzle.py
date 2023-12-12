#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import numpy as np
import collections
import itertools


def calc_a(input):
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
    gal = calc_a(input)
    combo = itertools.combinations(gal.keys(), 2)
    # print(f'{gal=}')
    for c in combo:
        rows = [gal[g][0] for g in c] # galaxy rows
        cols = [gal[g][1] for g in c] # galaxy columns
        d = max(rows) - min(rows) + max(cols) - min(cols)
        dist += d
        # print(f'{c=} {x=} {y=} {d=}')
    return dist


def calc_b(input):
    ary = []
    for line in input.splitlines():
        ary.append(list(line))
    a = np.array(ary)
    (rows, cols) = a.shape

    # Find empty space
    r_empty = []
    for i in range(rows):
        c = collections.Counter(a[i])
        if '.' in c and len(c) == 1: # empty space?
            r_empty.append(i)
    c_empty = []
    for i in range(cols):
        c = collections.Counter(a[:, i])
        if '.' in c and len(c) == 1: # empty space?
            c_empty.append(i)
    # print(f'{r_empty=} {c_empty=}')

    # Spot galaxies
    gal = {}
    for r in range(rows):
        for c in range(cols):
            if a[r, c] == '#':
                gal_no = len(gal)+1
                gal[gal_no] = (r, c)
    # print(f'{gal=}')
    return (gal, r_empty, c_empty)

def solve_b(input, penalty=1000000):
    dist = 0
    (gal, r_empty, c_empty) = calc_b(input)
    print(f'{r_empty=} {c_empty=}')
    combo = itertools.combinations(gal.keys(), 2)

    p = penalty -1 # empty space penalty
    for c in combo:
        row_bounds = [gal[g][0] for g in c] # galaxy rows
        col_bounds = [gal[g][1] for g in c] # galaxy columns
        rows = set(range(min(row_bounds), max(row_bounds))) # rows between galaxies
        cols = set(range(min(col_bounds), max(col_bounds))) # cols between galaxies
        d = len(rows) + len(cols)
        if p > 0:
            row_empty = len(rows.intersection(r_empty))
            col_empty = len(cols.intersection(c_empty))
            ep = (row_empty + col_empty) * p
        else:
            ep = 0
        dist += d + ep
        # print(f'{c=} {row_bounds=} {col_bounds=} {d=} {row_empty=} {col_empty=} {ep=}')

    return dist


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
