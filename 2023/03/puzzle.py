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


def calc_b(input):
    result = None
    return result


def solve_b(input):
    result = 0
    for line in input.split('\n'):
        result += calc_b(line)
    return str(result)


def main():
    day = get_day_and_year()[0]
    year = get_day_and_year()[1]
    p = Puzzle(day=day, year=year)

    result_a = solve_a(data)
    print(f'Answer A: {result_a}')
    p.answer_a = result_a

    result_b = solve_b(data)
    print(f'Answer B: {result_b}')
    p.answer_b = result_b


if __name__ == '__main__':
    main()
