#!/usr/bin/env python3

import regex as re
from aocd import data, get_day_and_year
from aocd.models import Puzzle


def calc_a(input):
    points = 0
    split = input.split(':')
    card_no = split[0].split(' ')[1]
    win_str = split[1].split('|')[0]
    have_str = split[1].split('|')[1]
    win = re.findall(r'(\d+)', win_str)
    have = re.findall(r'(\d+)', have_str)
    intersect = list(set(win).intersection(have))
    if len(intersect) > 0:
        points = 2**(len(intersect)-1)
    # print(f'{card_no=} {win=} {have=} {intersect=} {points=}')
    return points


def solve_a(input):
    result = 0
    for line in input.split('\n'):
        result += calc_a(line)
    return str(result)


def calc_b(input):
    split = input.split(':')
    # print(f'{split=}')
    card_no = int(re.search(r'(\d+)', split[0]).group(1))
    win_str = split[1].split('|')[0]
    have_str = split[1].split('|')[1]
    win = re.findall(r'(\d+)', win_str)
    have = re.findall(r'(\d+)', have_str)
    matches = len(list(set(win).intersection(have)))
    card_copies = list(range(card_no+1, card_no+matches+1))
    result = {
        'card_no': card_no,
        'card_copies': card_copies
    }
    print(f'{matches=} {card_copies=}')
    # print(result['card_copies'])
    return result


def solve_b(input):
    cards = {}
    for line in input.split('\n'):
        print(line)
        card = calc_b(line)
        card_no = card['card_no']
        if not card_no in cards:
            print(f'Card {card_no} not processed and no copies, setting count to 0 (line)')
            cards[card_no] = 0
        print(f'Incrementing count of card {card_no} by 1 from {cards[card_no]}')
        cards[card_no] += 1
        print(f'Count after: {cards[card_no]}')
        copies = card['card_copies']
        # print(f'{copies=}')
        for copy in copies:
            print(f'Counting copy of card {copy}')
            if not copy in cards:
                print(f'Card {copy} not processed and no copies, setting count to 0 (line)')
                cards[copy] = 0
            print(f'Incrementing count of card {copy} by number of {card} cards ({cards[card_no]}) from {cards[copy]}')
            cards[copy] += cards[card_no]
            print(f'Value after: {cards[copy]}')
        print()
    print(f'Number of cards: {len(cards)}')
    result = sum(cards.values())
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
