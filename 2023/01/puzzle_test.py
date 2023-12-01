import pytest
from puzzle import calc_a, solve_a, calc_b, solve_b
from aocd import get_day_and_year
from aocd.models import Puzzle


# Intermediate tests

calc_a_testdata = [
    ('1abc2', 12),
    ('pqr3stu8vwx', 38),
    ('a1b2c3d4e5f', 15),
    ('treb7uchet', 77)
]
@pytest.mark.parametrize('input,expected', calc_a_testdata)
def test_calc_a(input, expected):
    assert calc_a(input) == expected

calc_b_testdata = [
    ('two1nine', 29),
    ('eightwothree', 83),
    ('abcone2threexyz', 13),
    ('xtwone3four', 24),
    ('4nineeightseven2', 42),
    ('zoneight234', 14),
    ('7pqrstsixteen', 76)
]
@pytest.mark.parametrize('input,expected', calc_b_testdata)
def test_calc_b(input, expected):
    assert calc_b(input) == expected


# Solution tests

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

@pytest.mark.parametrize('input,expected', test_a)
def test_solve_a(input, expected):
    assert solve_a(input) == expected

# EXAMPLE NOT UPDATED!
example_b = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
def test_solve_b():
    assert solve_b(example_b) == "281"

