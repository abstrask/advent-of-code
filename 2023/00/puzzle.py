#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    result = None
    return result


def solve_a(input):
    result = 0
    for line in input.splitlines():
        result += calc_a(line)
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
