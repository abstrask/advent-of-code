#!/usr/bin/env python3

import regex as re
from alive_progress import alive_bar
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(max_time: int, dist_to_beat: int):
    max_times = []
    # print(f'{max_time=} {dist_to_beat=}')
    print()
    with alive_bar(max_time-1) as bar:
        for hold in range(1, max_time):
            speed = hold
            remain = max_time - hold
            dist = remain * speed
            won = dist > dist_to_beat # greater than or equal?
            # print(f'{hold=} {remain=} {dist=} {won=}')
            if won:
                max_times.append(hold)
            bar()
    result = len(max_times)
    # print(f'{result=}')
    return result


def solve_a(input):
    result = 0
    lines = input.split('\n')
    for line in lines:
        mode = re.search(r'^(\w+)', line).group(1)
        numbers = re.findall(r'(\d+)', line)
        # print(f'{mode=} {numbers=}')
        if mode == 'Time':
            times = numbers
        elif mode == 'Distance':
            dist = numbers

    # print(f'{times=} {dist=}')
    for idx, time in enumerate(times):
        wins = calc_a(max_time=int(time), dist_to_beat=int(dist[idx]))
        if result == 0:
            result = wins
        else:
            result *= wins
    return result


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
