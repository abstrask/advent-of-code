#!/usr/bin/env python3

import regex as re
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(line, above=None, below=None):
    # print(f'\n{line=} {above=} {below=}')
    result = []
    matches = re.finditer(r'(\d+)', line)
    for m in matches:
        span = m.span()
        part = int(m.group(0))

        try:
            begin = span[0]-1
            end = span[0]
            before = line[begin:end]
        except IndexError:
            before = ''
        try:
            begin = span[1]
            end = span[1]+1
            after = line[begin:end]
        except IndexError:
            after = ''

        low = max(span[0]-1, 0)
        if above:
            high_above = min(span[1]+1, len(above))
            adj_above = above[low:high_above]
        else:
            adj_above = ''
        if below:
            high_below = min(span[1]+1, len(below))
            adj_below = below[low:high_below]
        else:
            adj_below = ''
        adjacent = before + after + adj_above + adj_below

        if re.search(r'[^\.\d]', adjacent):
            to_add = part
        else:
            to_add = 0

        result.append({
            'span': span,
            'part': part,
            'before': before,
            'after': after,
            'adj_above': adj_above,
            'adj_below': adj_below,
            'adjacent': adjacent,
            'to_add': to_add
        })
    # print(f'{result}')
    return result


def solve_a(input):
    result = 0
    lines = input.split('\n')
    for i, line in enumerate(lines):
        if i > 0:
            above = lines[i-1]
        else:
            above = None
        try:
            below = lines[i+1]
        except IndexError:
            below = None
        # print(f'{line=} {above=} {below=}')
        parts = calc_a(line=line, above=above, below=below)
        for p in parts:
            result += p['to_add']
    return result


def find_gears(line_no: int, line: str, x_offset: int):
    pos = []
    matches = re.finditer(r'[\*]', line)
    for m in matches:
        x = m.span()[0] + x_offset
        pos.append((line_no, x))
    return pos


def calc_b(line_no: int, line: str, above=None, below=None, gears={}):
    # print(f'\n{line=} {above=} {below=}')
    matches = re.finditer(r'(\d+)', line)
    for m in matches:
        g_pos = []
        span = m.span()
        part = int(m.group(0))

        # Get char next to number (before/after)
        try:
            begin = span[0]-1
            end = span[0]
            before = line[begin:end]
            if before == '*': # find gear
                g_pos += [(line_no, begin)]
        except IndexError:
            before = ''
        try:
            begin = span[1]
            end = span[1]+1
            after = line[begin:end]
            if after == '*': # find gear
                g_pos += [(line_no, begin)]
        except IndexError:
            after = ''

        # Get strings adjacent to number above and below
        low = max(span[0]-1, 0)
        if above:
            high_above = min(span[1]+1, len(above))
            adj_above = above[low:high_above]
            g_pos += find_gears(line_no=line_no-1, line=adj_above, x_offset=low)
        else:
            adj_above = ''
        if below:
            high_below = min(span[1]+1, len(below))
            adj_below = below[low:high_below]
            g_pos += find_gears(line_no=line_no+1, line=adj_below, x_offset=low)
        else:
            adj_below = ''

        for g in g_pos:
            if not g in gears:
                gears[g] = []
            gears[g].append(part)

    return gears


def solve_b(input):
    result = 0
    gears = {}
    lines = input.split('\n')
    for line_no, line in enumerate(lines):
        if line_no > 0:
            above = lines[line_no-1]
        else:
            above = None
        try:
            below = lines[line_no+1]
        except IndexError:
            below = None
        gears = calc_b(line_no=line_no, line=line, above=above, below=below, gears=gears)
    # print(f'{gears=}')

    for p, g in gears.items():
        if len(g) == 2:
            result += g[0] * g[1]

    return result


def main():
    day = get_day_and_year()[0]
    year = get_day_and_year()[1]
    p = Puzzle(day=day, year=year)

    if not p.answered_a:
        result_a = solve_a(data)
        print(f'Answer A: {result_a}')
        p.answer_a = result_a

    if not p.answered_b:
        result_b = solve_b(data)
        print(f'Answer B: {result_b}')
        p.answer_b = result_b


if __name__ == '__main__':
    main()
