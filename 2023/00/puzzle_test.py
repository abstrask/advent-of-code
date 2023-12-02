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
    ('0', 0)
]
@pytest.mark.parametrize('input,expected', calc_a_testdata)
def test_calc_a(input, expected):
    assert calc_a(input) == expected

calc_b_testdata = [
    ('0', 0)
]
@pytest.mark.parametrize('input,expected', calc_b_testdata)
def test_calc_b(input, expected):
    assert calc_b(input) == expected


# Solution tests

@pytest.mark.parametrize('input,expected', test_a, ids="example")
def test_solve_a(input, expected):
    assert solve_a(input) == expected

# EXAMPLE NOT UPDATED!
example_b = """0
0
0"""
def test_solve_b():
    assert solve_b(example_b) == "000"

