#!/usr/bin/env python3

from aocd import data, get_day_and_year
from aocd.models import Puzzle
import regex as re
import math


def calc_a(input):
    result = None
    return result


def solve_a(input):
    result = 0
    nodes = {}
    for i, line in enumerate(input.split('\n')):
        if len(line.strip()) == 0:
            continue
        if i == 0:
            ops = []
            for c in line:
                if c == 'L':
                    op = 0
                else:
                    op = 1
                ops.append(op)
            # print(f'{ops=}')
            continue

        split = line.split(' = ')
        key = split[0]
        m = re.search(r'(\w+), (\w+)', split[1])
        val = (m.group(1), m.group(2))
        nodes[key] = val

    # print(f'{nodes=}')
    steps = 0
    pos = 'AAA'
    while True:
        op = ops[steps % len(ops)]
        pos_tuple = nodes[pos]
        next_pos = pos_tuple[op]
        steps += 1
        # print(f'{steps=} {op=} {pos=} {next_pos=}')
        pos = next_pos
        if pos == 'ZZZ':
            break

    return steps


def calc_b(input):
    result = None
    return result


def solve_b(input):

    # Populate nodes
    nodes = {}
    for i, line in enumerate(input.split('\n')):
        if len(line.strip()) == 0:
            continue
        if i == 0:
            ops = []
            for c in line:
                if c == 'L':
                    op = 0
                else:
                    op = 1
                ops.append(op)
            # print(f'{ops=}')
            continue

        split = line.split(' = ')
        key = split[0]
        m = re.search(r'(\w+), (\w+)', split[1])
        val = (m.group(1), m.group(2))
        nodes[key] = val

    # Determine periods
    char = 'A'
    pos = {}
    for p in [k for k in nodes.keys() if k[-1] == char]:
        pos[p] = p
    print(f'{pos=}')

    print()
    step = 1
    periods = {}
    while True:
        op = ops[(step-1) % len(ops)]

        if step % 1000 == 0:
            print(f'{periods=}')

        # All periods found?
        if len(periods) == len(pos):
            break

        for k, p in pos.items():
            # print(f'{k=} {p=}')
            if p[-1] == 'Z':
                continue
            pos_tuple = nodes[p] # Look up tuple for last position in dict
            next_pos = pos_tuple[op]
            # print(f'{step=} {op=} {pos=} {next_pos=}')
            if next_pos[-1] == 'Z':
            # if next_pos == k:
                print(f'{k=} {step=}')
                periods[k] = step
            pos[k] = next_pos
            # print(f'{pos=}')

        step += 1

    print(f'{periods=}')

    # Get lowest cmmmon multiple of periods
    # print(list(periods.values()))
    result = math.lcm(*periods.values())

    return result

# periods={'JPA': 21251, 'QJA': 14257, 'VNA': 15871, 'DPA': 16409, 'DBA': 21251, 'AAA': 21251}
# Answer B: 4053564497
# aocd will not submit that answer again. At 2023-12-10 11:01:13.555442-05:00 you've previously submitted 4053564497 and the server responded with:
# That's not the right answer; your answer is too low.  If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit.  Please wait one minute before trying again. [Return to Day 8]



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
