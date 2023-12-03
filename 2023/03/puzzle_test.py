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

calc_a_parts_testdata = [
    ('467..114..', [467, 114]),
    ('...*......', []),
    ('..35..633.', [35, 633]),
    ('......#...', []),
    ('617*......', [617]),
    ('.....+.58.', [58]),
    ('..592.....', [592]),
    ('......755.', [755]),
    ('...$.*....', []),
    ('.664.598..', [664, 598])
]
@pytest.mark.parametrize('input,expected', calc_a_parts_testdata)
def test_calc_a_parts(input, expected):
    assert [m['part'] for m in calc_a(input)] == expected


calc_a_spans_testdata = [
    ('467..114..', [(0,3), (5,8)]),
    ('...*......', []),
    ('..35..633.', [(2,4), (6,9)]),
    ('......#...', []),
    ('617*......', [(0,3)]),
    ('.....+.58.', [(7,9)]),
    ('..592.....', [(2,5)]),
    ('......755.', [(6,9)]),
    ('...$.*....', []),
    ('.664.598..', [(1,4), (5,8)])
]
@pytest.mark.parametrize('input,expected', calc_a_spans_testdata)
def test_calc_a_spans(input, expected):
    assert [m['span'] for m in calc_a(input)] == expected


calc_a_add_testdata = [
    ({
        'line':  '467..114..',
        'below': '...*......'
    }, 467),
    ({
        'above': '...*......',
        'line':  '..35..633.',
        'below': '......#...'
    }, 668),
    ({
        'above': '......#...',
        'line':  '617*......',
        'below': '.....+.58.'
    }, 617),
    ({
        'above': '617*......',
        'line':  '.....+.58.',
        'below': '..592.....'
    }, 0),
    ({
        'above': '.....+.58.',
        'line':  '..592.....',
        'below': '......755.'
    }, 592),
    ({
        'above': '..592.....',
        'line':  '......755.',
        'below': '...$.*....'
    }, 755),
    ({
        'above': '...$.*....',
        'line':  '.664.598..'
    }, 1262)
]
@pytest.mark.parametrize('input,expected', calc_a_add_testdata)
def test_calc_a_add(input, expected):
    assert sum([m['to_add'] for m in calc_a(**input)]) == expected


# calc_a_testdata_adjacent = [
#     ('467..114..', ['.']),
#     ('...*......', []),
#     ('..35..633.', ['..', '..']),
#     ('......#...', []),
#     ('617*......', ['*']),
#     ('.....+.58.', ['..']),
#     ('..592.....', ['..']),
#     ('......755.', ['..']),
#     ('...$.*....', []),
#     ('.664.598..', [(1,4), (5,8)])
# ]
# @pytest.mark.parametrize('input,expected', calc_a_testdata_spans)
# def test_calc_a_spans(input, expected):
#     assert [m['span'] for m in calc_a(input)] == expected


# calc_b_testdata = [
#     ('0', 0)
# ]
# @pytest.mark.parametrize('input,expected', calc_b_testdata)
# def test_calc_b(input, expected):
#     assert calc_b(input) == expected


# # Solution tests

@pytest.mark.parametrize('input,expected', test_a, ids=['example'])
def test_solve_a(input, expected):
    assert str(solve_a(input)) == expected

# # EXAMPLE NOT UPDATED!
# example_b = """0
# 0
# 0"""
# def test_solve_b():
#     assert solve_b(example_b) == "000"

