#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import regex as re


def calc_a(input):
    result = None
    return result


def solve_a(input):
    result = 0
    nodes = {}
    for i, line in enumerate(input.split('\n')):
        if len(line.strip()) == 0:
            continue
        if i == 0:
            ops = []
            for c in line:
                if c == 'L':
                    op = 0
                else:
                    op = 1
                ops.append(op)
            # print(f'{ops=}')
            continue

        split = line.split(' = ')
        key = split[0]
        m = re.search(r'(\w+), (\w+)', split[1])
        val = (m.group(1), m.group(2))
        nodes[key] = val

    # print(f'{nodes=}')
    steps = 0
    pos = 'AAA'
    while True:
        op = ops[steps % len(ops)]
        pos_tuple = nodes[pos]
        next_pos = pos_tuple[op]
        steps += 1
        # print(f'{steps=} {op=} {pos=} {next_pos=}')
        pos = next_pos
        if pos == 'ZZZ':
            break

    return steps


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
