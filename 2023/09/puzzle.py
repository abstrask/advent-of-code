#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import regex as re


def recursive(seq, first=[], last=[]):
    diff = [seq[i+1] - v for i, v in enumerate(seq[:-1])]
    first.append(seq[0])
    last.append(seq[-1])
    # print(f'{seq=} {diff=} {first=} {last=}')
    if not all(d == 0 for d in diff):
        return recursive(diff, first, last)
    else:
        prev = 0
        while len(first) > 0:
            prev = first.pop() - prev
        return (prev, sum(last))


def calc_a(input):
    seq = [int(m) for m in re.findall(r'(-*\d+)', input)]
    # print()
    result = recursive(seq, [], [])[1]
    return result


def solve_a(input):
    result = 0
    for line in input.splitlines():
        result += calc_a(line)
    return result


def calc_b(input):
    seq = [int(m) for m in re.findall(r'(-*\d+)', input)]
    # print()
    result = recursive(seq, [], [])[0]
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
