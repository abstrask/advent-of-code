#!/usr/bin/env python3

import numpy as np
from collections import Counter
from alive_progress import alive_bar
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    card_val = {'A': '14', 'K': '13', 'Q': '12', 'J': '11', 'T': '10', '9': '09', '8': '08', '7': '07', '6': '06', '5': '05', '4': '04', '3': '03', '2': '02'}
    # Range digits:
    # First: Hand type rank (five, four, house, three, two pairs, pair, single)
    # Subsequent: Each card value padded to 2 digits
    hand = Counter(input)
    card_count = hand.values()

    if 5 in card_count: # 5 of a kind
        type_val = 7
    elif 4 in card_count: # 4 of a kind
        type_val = 6
    elif 3 in card_count and 2 in card_count: # full house
        type_val = 5
    elif 3 in card_count: # 3 of a kind
        type_val = 4
    elif 2 in Counter(card_count).values(): # two pairs
        type_val = 3
    elif 2 in card_count: # one pair
        type_val = 2
    else:
        type_val = 1
    # print(f'{input=} {hand=} {card_count=} {type_val=}')
    hand_val = str(type_val) + card_val[input[0]] + card_val[input[1]] + card_val[input[2]] + card_val[input[3]] + card_val[input[4]]
    return int(hand_val)


def solve_a(input):
    result = 0
    lines = input.split('\n')
    hand_vals = {}
    print()
    with alive_bar(len(lines)) as bar:
        for line in lines:
            split = line.split(' ')
            hand = split[0]
            bid = int(split[1])
            # print(f'{line=} {hand=} {bid=}')
            hand_vals[calc_a(hand)] = bid
            bar()
    # print(f'{hand_vals=}')

    print(f'Sorting hands')
    bids = [hand_vals[key] for key in sorted(hand_vals.keys())]
    # print(f'{bids=}')

    print(f'Calculating winnings')
    for idx, bid in enumerate(bids):
        rank = idx + 1
        win = rank * bid
        # print(f'{rank=} {bid=} {win=}')
        result += win
    return result


def calc_b(input):
    card_val = {'A': '14', 'K': '13', 'Q': '12', 'T': '10', '9': '09', '8': '08', '7': '07', '6': '06', '5': '05', '4': '04', '3': '03', '2': '02', 'J': '01'}
    hand = Counter(input)
    jokers = hand['J']
    most_common = [ x[1] for x in hand.most_common(3) if x[0] != 'J'][:2] # non-jokers
    if len(most_common) == 0:
        most_common = [0] # hand only contains jokers
    print(f'{input=} {hand=} {jokers=} {most_common=}')

    # Full house or 2 pairs?
    for i, c in enumerate(most_common):
        if i == 0:
            need_jokers_house = max([3-c, 0])
            need_jokers_two_pairs = max([2-c, 0])
        else:
            need_jokers_house += max([2-c, 0])
            need_jokers_two_pairs += max([2-c, 0])

    if most_common[0] + jokers >= 5: # 5 of a kind
        type = '5 of a kind'
        type_val = 7
    elif most_common[0] + jokers == 4: # 4 of a kind
        type = '4 of a kind'
        type_val = 6
    elif need_jokers_house <= jokers: # full house
        type = 'Full house'
        type_val = 5
    elif most_common[0] + jokers == 3: # 3 of a kind
        type = '3 of a kind'
        type_val = 4
    elif need_jokers_two_pairs <= jokers: # two pairs
        type = '2 pairs'
        type_val = 3
    elif most_common[0] + jokers == 2: # one pair
        type = '1 pair'
        type_val = 2
    else:
        type = 'Single'
        type_val = 1
    # print(f'{type_val=} {type=}')
    hand_val = str(type_val) + card_val[input[0]] + card_val[input[1]] + card_val[input[2]] + card_val[input[3]] + card_val[input[4]]
    return int(hand_val)


def solve_b(input):
    result = 0
    lines = input.split('\n')
    hand_vals = {}
    print()
    with alive_bar(len(lines)) as bar:
        for line in lines:
            split = line.split(' ')
            hand = split[0]
            bid = int(split[1])
            # print(f'{line=} {hand=} {bid=}')
            hand_vals[calc_b(hand)] = bid
            bar()
    # print(f'{hand_vals=}')

    print(f'Sorting hands')
    bids = [hand_vals[key] for key in sorted(hand_vals.keys())]
    # print(f'{bids=}')

    print(f'Calculating winnings')
    for idx, bid in enumerate(bids):
        rank = idx + 1
        win = rank * bid
        # print(f'{rank=} {bid=} {win=}')
        result += win
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
