#!/usr/bin/env python3

import regex as re
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    result = {}
    matches = re.findall(r'(\d+)', input)
    source = int(matches[1])
    dest = int(matches[0])
    length = int(matches[2])
    # print(f'{source=} {dest=} {length=}')
    for i in range(0, length):
        result[source + i] = dest + i
    return result


def solve_a(input):
    result = 0
    seed_to_soil = {}
    soil_to_fert = {}
    fert_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_hum = {}
    hum_to_loc = {}

    for line in input.split('\n'):
        if line.strip() == '':
            continue

        if ':' in line:
            split = line.split(':')
            mode = split[0].strip()
            if mode == 'seeds': # only seeds are provided on same line
                seeds = []
                matches = re.findall(r'(\d+)', split[1])
                for m in matches:
                    seeds.append(int(m))
                print(f'{seeds=}')
            continue

        # print(f'{mode=} {line=}')

        match mode:
            case 'seed-to-soil map':
                seed_to_soil = seed_to_soil | calc_a(line)

            case 'soil-to-fertilizer map':
                soil_to_fert = soil_to_fert | calc_a(line)

            case 'fertilizer-to-water map':
                fert_to_water = fert_to_water | calc_a(line)

            case 'water-to-light map':
                water_to_light = water_to_light | calc_a(line)

            case 'light-to-temperature map':
                light_to_temp = light_to_temp | calc_a(line)

            case 'temperature-to-humidity map':
                temp_to_hum = temp_to_hum | calc_a(line)

            case 'humidity-to-location map':
                 hum_to_loc = hum_to_loc | calc_a(line)

            case _:
                raise 'hell'

    # print(f'{seed_to_soil=}')
    # print(f'{soil_to_fert=}')
    # print(f'{fert_to_water=}')
    # print(f'{water_to_light=}')
    # print(f'{light_to_temp=}')
    # print(f'{temp_to_hum=}')
    # print(f'{hum_to_loc=}')

    print(f'Looking up seeds...')
    locations = []
    for s in seeds:
        try:
            soil = seed_to_soil[s]
        except KeyError:
            soil = s
        try:
            fert = soil_to_fert[soil]
        except KeyError:
            fert = soil
        try:
            water = fert_to_water[fert]
        except KeyError:
            water = fert
        try:
            light = water_to_light[water]
        except KeyError:
            light = water
        try:
            temp = light_to_temp[light]
        except KeyError:
            temp = light
        try:
            hum = temp_to_hum[temp]
        except KeyError:
            hum = temp
        try:
            loc = hum_to_loc[hum]
        except KeyError:
            loc = hum
        # print(f'{s=} {soil=} {fert=} {water=} {light=} {temp=} {hum=} {loc=}')
        locations.append(loc)

    result = min(locations)

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
