import pytest
from puzzle import calc_a, solve_a, calc_b, solve_b
from aocd import get_day_and_year
from aocd.models import Puzzle

# Setup

day = get_day_and_year()[0]
year = get_day_and_year()[1]
p = Puzzle(day=day, year=year)

test_a = []
test_b = []
for e in p.examples:
    print(e)
    if e.answer_a:
        test_a.append((e.input_data, e.answer_a))
    if e.answer_b:
        test_b.append((e.input_data, e.answer_b))

if test_a:
    for t in test_a:
        print(f'\nInput A:\n{t[0]}')
        print(f'Expected A: {t[1]}')
if test_b:
    for t in test_b:
        print(f'\nInput B:\n{t[0]}')
        print(f'Expected B: {t[1]}')


# Intermediate tests

calc_a_testdata = [
    ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', True),
    ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', True),
    ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', False),
    ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', False),
    ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', True)
]
@pytest.mark.parametrize('input,expected', calc_a_testdata)
def test_calc_a(input, expected):
    assert calc_a(input)['possible'] == expected

calc_b_testdata = [
    ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 48),
    ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 12),
    ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 1560),
    ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 630),
    ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', 36)
]
@pytest.mark.parametrize('input,expected', calc_b_testdata)
def test_calc_b(input, expected):
    assert calc_b(input) == expected


# Solution tests

range_a = range(0, len(test_a))
@pytest.mark.parametrize('input,expected', test_a, ids=range_a)
def test_solve_a(input, expected):
    assert str(solve_a(input)) == expected

# EXAMPLE NOT UPDATED!
example_b = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

range_b = range(0, len(test_b))
def test_solve_b():
    assert solve_b(example_b) == 2286
