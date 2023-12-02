#!/usr/bin/env python3

import regex as re # 're' does not support overlapping matches
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    m = re.findall(r'(\d)', input)
    result = f'{m[0]}{m[-1]}'
    return int(result)


def solve_a(input):
    result = 0
    for line in input.split('\n'):
        result += calc_a(line)
    return str(result)


def calc_b(input):
    replace = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    numbers = '|'.join(replace.keys())
    regex_str = r'(\d|' + numbers + ')'
    matches = re.findall(regex_str, input, overlapped=True)
    digits = ''
    for m in matches:
        if m in replace.keys():
            digits += replace[m]
        else:
            digits += m
    result = f'{digits[0]}{digits[-1]}'
    print(f'{result} <- {digits} <- {input}')
    return int(result)


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
