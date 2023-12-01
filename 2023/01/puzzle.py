#!/usr/bin/env python3

import re
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    m = re.findall(r'(\d)', input)
    solution = f'{m[0]}{m[-1]}'
    return int(solution)


def solve_a(input):
    solution = 0
    for line in input.split('\n'):
        solution += calc_a(line)
    return str(solution)


def calc_b(input):
    return


def solve_b(input):
    pass


def main():
    day = get_day_and_year()[0]
    year = get_day_and_year()[1]
    p = Puzzle(day=day, year=year)

    result_a = solve_a(data)
    print(f'\nAnswer A: {result_a}')
    p.answer_a = result_a

    # result_b = solve_b(data.split('\n'))
    # print(f'\nAnswer B: {result_b}')
    # p.answer_b = result_b

    # p.answered_a
    # p.answered_b


if __name__ == '__main__':
    main()
