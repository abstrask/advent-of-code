#!/usr/bin/env python3

import regex as re
import math
import matplotlib.pyplot as plt
from alive_progress import alive_bar
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(max_time: int, dist_to_beat: int, plot=False):
    # max_times = []
    wins = 0
    times = list(range(1, max_time))
    # print(f'{max_time=} {dist_to_beat=}')
    print()
    with alive_bar(max_time-1) as bar:
        dists = []
        for hold in times:
            speed = hold
            remain = max_time - hold
            dist = remain * speed
            if plot:
                dists.append(dist)
            won = dist > dist_to_beat # greater than or equal?
            # print(f'{hold=} {remain=} {dist=} {won=}')
            if won:
                # max_times.append(hold)
                wins += 1
            bar()
    if plot:
        plt.plot(times, dists, linestyle='-')
        plt.xlabel('Hold time (ms)')
        plt.ylabel('Distance (mm)')
        plt.axhline(y=dist_to_beat, color='r', linestyle='--', label='Distance to beat')
        plt.show()
    # result = len(max_times)
    # print(f'{result=}')
    return wins


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


def calc_b(max_time: int, dist_to_beat: int):
    # Distance follows a parabola, where is x is hold time: y = -x^2 + max_time*x
    # If we subtract dist_to_beat, we can calculate the roots of the parabola
    # Any hold time between the roots are wins.
    # a: -1, b: max_time, c: dist_to_beat

    discriminant = max_time**2 - (4 * dist_to_beat) # b^2-4ac, but a is always -1
    sqrt_disc = math.sqrt(discriminant)
    # print(f'{discriminant=}')

    if discriminant <= 0:
        return 0
    else:
        root1 = (-max_time - sqrt_disc) / -2
        root2 = (-max_time + sqrt_disc) / -2
    # print(f'{root1=} {root2=}')
    wins = math.floor(max([root1, root2])) - math.ceil(min([root1, root2])) + 1

    return wins


def solve_b(input):
    lines = input.split('\n')
    for line in lines:
        split = line.replace(' ', '').split(':')
        if split[0] == 'Time':
            time = int(split[1])
        elif split[0] == 'Distance':
            dist = int(split[1])
    wins = calc_b(max_time=time, dist_to_beat=dist)
    return wins


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
