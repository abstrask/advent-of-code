#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import regex as re


def rec_a(seq, last=[]):
    diff = [seq[i+1] - v for i, v in enumerate(seq[:-1])]
    # print(f'{seq=} {diff=} {last=}')
    last.append(seq[-1])
    if not all(d == 0 for d in diff):
        return rec_a(diff, last)
    else:
        return sum(last)


def calc_a(input):
    seq = [int(m) for m in re.findall(r'(-*\d+)', input)]
    result = rec_a(seq, [])
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
