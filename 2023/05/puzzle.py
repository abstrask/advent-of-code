#!/usr/bin/env python3

import regex as re
from alive_progress import alive_bar
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def str_to_map(input):
    result = {}
    for line in input.split('\n'):
        matches = re.findall(r'(\d+)', line)
        source = int(matches[1])
        dest = int(matches[0])
        length = int(matches[2])
        # print(f'{source=} {dest=} {length=}')
        result[source] = {
            'length': length,
            'dest': dest
        }
    # print(result)
    return result


def get_dest(source: int, map: map):
    dest = source
    for k, v in map.items():
        # print(f'{k=} {v=}')
        if k <= source < k + v['length']:
            dest = source - k + v['dest']
            break
    # print(f'{source=} {dest=}')
    return dest


def solve_a(input):
    result = 0
    seed_to_soil_lines = []
    soil_to_fert_lines = []
    fert_to_water_lines = []
    water_to_light_lines = []
    light_to_temp_lines = []
    temp_to_hum_lines = []
    hum_to_loc_lines = []

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
                seed_to_soil_lines.append(line)

            case 'soil-to-fertilizer map':
                soil_to_fert_lines.append(line)

            case 'fertilizer-to-water map':
                fert_to_water_lines.append(line)

            case 'water-to-light map':
                water_to_light_lines.append(line)

            case 'light-to-temperature map':
                light_to_temp_lines.append(line)

            case 'temperature-to-humidity map':
                temp_to_hum_lines.append(line)

            case 'humidity-to-location map':
                hum_to_loc_lines.append(line)

            case _:
                raise 'hell'

    seed_to_soil = str_to_map('\n'.join(seed_to_soil_lines))
    soil_to_fert = str_to_map('\n'.join(soil_to_fert_lines))
    fert_to_water = str_to_map('\n'.join(fert_to_water_lines))
    water_to_light = str_to_map('\n'.join(water_to_light_lines))
    light_to_temp = str_to_map('\n'.join(light_to_temp_lines))
    temp_to_hum = str_to_map('\n'.join(temp_to_hum_lines))
    hum_to_loc = str_to_map('\n'.join(hum_to_loc_lines))

    # print(f'{seed_to_soil=}')
    # print(f'{soil_to_fert=}')
    # print(f'{fert_to_water=}')
    # print(f'{water_to_light=}')
    # print(f'{light_to_temp=}')
    # print(f'{temp_to_hum=}')
    # print(f'{hum_to_loc=}')

    locations = []
    for s in seeds:
        try:
            soil = get_dest(source=s, map=seed_to_soil)
        except KeyError:
            soil = s
        try:
            fert = get_dest(source=soil, map=soil_to_fert)
        except KeyError:
            fert = soil
        try:
            water = get_dest(source=fert, map=fert_to_water)
        except KeyError:
            water = fert
        try:
            light = get_dest(source=water, map=water_to_light)
        except KeyError:
            light = water
        try:
            temp = get_dest(source=light, map=light_to_temp)
        except KeyError:
            temp = light
        try:
            hum = get_dest(source=temp, map=temp_to_hum)
        except KeyError:
            hum = temp
        try:
            loc = get_dest(source=hum, map=hum_to_loc)
        except KeyError:
            loc = hum
        # print(f'{s=} {soil=} {fert=} {water=} {light=} {temp=} {hum=} {loc=}')
        locations.append(loc)

    result = min(locations)

    return result

# Brute-forced 1.835.328.022 seeds in 2h 41m 31s :-|

def solve_b(input):
    result = 0
    seed_to_soil_lines = []
    soil_to_fert_lines = []
    fert_to_water_lines = []
    water_to_light_lines = []
    light_to_temp_lines = []
    temp_to_hum_lines = []
    hum_to_loc_lines = []

    for line in input.split('\n'):
        if line.strip() == '':
            continue

        if ':' in line:
            split = line.split(':')
            mode = split[0].strip()
            if mode == 'seeds': # only seeds are provided on same line
                seed_str = split[1]
            continue

        # print(f'{mode=} {line=}')

        match mode:
            case 'seed-to-soil map':
                seed_to_soil_lines.append(line)

            case 'soil-to-fertilizer map':
                soil_to_fert_lines.append(line)

            case 'fertilizer-to-water map':
                fert_to_water_lines.append(line)

            case 'water-to-light map':
                water_to_light_lines.append(line)

            case 'light-to-temperature map':
                light_to_temp_lines.append(line)

            case 'temperature-to-humidity map':
                temp_to_hum_lines.append(line)

            case 'humidity-to-location map':
                hum_to_loc_lines.append(line)

            case _:
                raise 'hell'

    seed_to_soil = str_to_map('\n'.join(seed_to_soil_lines))
    soil_to_fert = str_to_map('\n'.join(soil_to_fert_lines))
    fert_to_water = str_to_map('\n'.join(fert_to_water_lines))
    water_to_light = str_to_map('\n'.join(water_to_light_lines))
    light_to_temp = str_to_map('\n'.join(light_to_temp_lines))
    temp_to_hum = str_to_map('\n'.join(temp_to_hum_lines))
    hum_to_loc = str_to_map('\n'.join(hum_to_loc_lines))

    # print(f'{seed_to_soil=}')
    # print(f'{soil_to_fert=}')
    # print(f'{fert_to_water=}')
    # print(f'{water_to_light=}')
    # print(f'{light_to_temp=}')
    # print(f'{temp_to_hum=}')
    # print(f'{hum_to_loc=}')

    seed_ranges = []
    matches = re.findall(r'(\d+)', seed_str)
    for idx in range(0, len(matches), 2):
        seed_begin = int(matches[idx])
        seed_count = int(matches[idx+1])
        seed_end = seed_begin + seed_count
        # print(f'{seed_begin=} {seed_end=} {seed_count=}')
        seed_ranges.append((seed_begin, seed_end))
    # print(f'{seed_ranges=}')

    locations = []
    for idx, sr in enumerate(seed_ranges):
        seed_begin = sr[0]
        seed_end = sr[1]
        seed_count = seed_end - seed_begin
        print(f'Processing range {idx+1} of {len(seed_ranges)}')
        with alive_bar(seed_count) as bar:
            for s in range(seed_begin, seed_end):
                # print(s)
                try:
                    soil = get_dest(source=s, map=seed_to_soil)
                except KeyError:
                    soil = s
                try:
                    fert = get_dest(source=soil, map=soil_to_fert)
                except KeyError:
                    fert = soil
                try:
                    water = get_dest(source=fert, map=fert_to_water)
                except KeyError:
                    water = fert
                try:
                    light = get_dest(source=water, map=water_to_light)
                except KeyError:
                    light = water
                try:
                    temp = get_dest(source=light, map=light_to_temp)
                except KeyError:
                    temp = light
                try:
                    hum = get_dest(source=temp, map=temp_to_hum)
                except KeyError:
                    hum = temp
                try:
                    loc = get_dest(source=hum, map=hum_to_loc)
                except KeyError:
                    loc = hum
                # print(f'{s=} {soil=} {fert=} {water=} {light=} {temp=} {hum=} {loc=}')
                locations.append(loc)
                bar()

    result = min(locations)

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
