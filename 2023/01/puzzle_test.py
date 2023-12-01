import pytest
from puzzle import solve_a, solve_b, calc_a, calc_b
from aocd import get_day_and_year
from aocd.models import Puzzle


# Manual intermediate tests

def test_calc_a_1():
    assert calc_a('1abc2') == 12

def test_calc_a_2():
    assert calc_a('pqr3stu8vwx') == 38

def test_calc_a_3():
    assert calc_a('a1b2c3d4e5f') == 15

def test_calc_a_4():
    assert calc_a('treb7uchet') == 77


# Automatic solution tests

day = get_day_and_year()[0]
year = get_day_and_year()[1]
p = Puzzle(day=day, year=year)

test_a = []
test_b = []
for e in p.examples:
    if e.answer_a:
        test_a.append((e.input_data, e.answer_a))
    if e.answer_b:
        test_b.append((e.input_data, e.answer_b))

@pytest.mark.parametrize('input,expected', test_a)
def test_solve_a(input, expected):
    assert solve_a(input) == expected

@pytest.mark.parametrize('input,expected', test_b)
def test_solve_b(input, expected):
    assert solve_b(input) == expected

