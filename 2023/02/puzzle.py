#!/usr/bin/env python3

# import regex as re
import re
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    TOTAL_RED = 12
    TOTAL_GREEN = 13
    TOTAL_BLUE = 14
    parts = input.split(': ')
    game = int(re.match(r'^Game (\d+)', parts[0]).group(1))
    possible = True
    sets = []
    sets_str = parts[1].split('; ')
    for s in sets_str:
        try:
            red = int(re.search(r'(\d+) red', s).group(1))
            if red > TOTAL_RED:
                possible = False
        except AttributeError:
            red = 0
        try:
            green = int(re.search(r'(\d+) green', s).group(1))
            if green > TOTAL_GREEN:
                possible = False
        except AttributeError:
            green = 0
        try:
            blue = int(re.search(r'(\d+) blue', s).group(1))
            if blue > TOTAL_BLUE:
                possible = False
        except AttributeError:
            blue = 0
        # sets.append({
        #     'red': red,
        #     'green': green,
        #     'blue': blue
        # })
    # print(f'\n{game=} {possible=}')
    result = {
        'game_id': game,
        'possible': possible
    }
    return result


def solve_a(input):
    result = 0
    # print(input)
    for line in input.split('\n'):
        game = calc_a(line)
        if game['possible']:
            result += game['game_id']
    return result


def calc_b(input):
    min_red = 0
    min_green = 0
    min_blue = 0
    parts = input.split(': ')
    sets_str = parts[1].split('; ')
    for s in sets_str:
        try:
            red = int(re.search(r'(\d+) red', s).group(1))
            min_red = max(red, min_red)
        except AttributeError:
            red = 0
        try:
            green = int(re.search(r'(\d+) green', s).group(1))
            min_green = max(green, min_green)
        except AttributeError:
            green = 0
        try:
            blue = int(re.search(r'(\d+) blue', s).group(1))
            min_blue = max(blue, min_blue)
        except AttributeError:
            blue = 0
    # print(f'{min_red=} {min_green=} {min_blue=}')
    result = min_red * min_green * min_blue
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
    p.answer_a = result_a

    result_b = solve_b(data)
    print(f'Answer B: {result_b}')
    p.answer_b = result_b


if __name__ == '__main__':
    main()
