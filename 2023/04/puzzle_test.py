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
    ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', 8),
    ('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', 2),
    ('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', 2),
    ('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', 1),
    ('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36', 0),
    ('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11', 0)
]
@pytest.mark.parametrize('test_input,expected', calc_a_testdata)
def test_calc_a(test_input, expected):
    assert calc_a(test_input) == expected

calc_b_testdata = [
    ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', [2,3,4,5]),
    ('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', [3,4]),
    ('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', [4,5]),
    ('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', [5]),
    ('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36', []),
    ('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11', [])
]
@pytest.mark.parametrize('test_input,expected', calc_b_testdata)
def test_calc_b(test_input, expected):
    assert calc_b(test_input)['card_copies'] == expected


# # Solution tests

@pytest.mark.parametrize('test_input,expected', test_a, ids=["example"])
def test_solve_a(test_input, expected):
    assert str(solve_a(test_input)) == expected

@pytest.mark.parametrize('test_input,expected', test_b, ids=["example"])
def test_solve_b(test_input, expected):
    assert str(solve_b(test_input)) == expected
