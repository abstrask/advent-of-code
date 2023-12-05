import pytest
from puzzle import solve_a, solve_b, str_to_map, get_dest
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



# PART A

# Intermediate tests

str_to_map_testdata = [
    ('''50 98 2
52 50 48''', {
        98: {'length': 2, 'dest': 50},
        50: {'length': 48, 'dest': 52}
    }),
    ('''0 15 37
37 52 2
39 0 15''', {
        15: {'length': 37, 'dest': 0},
        52: {'length': 2, 'dest': 37},
        0: {'length': 15, 'dest': 39}
    })
]
@pytest.mark.parametrize('test_input,expected', str_to_map_testdata)
def test_str_to_map(test_input, expected):
    assert str_to_map(test_input) == expected

get_dest_testmap = {
    15: {'length': 37, 'dest': 0},
    52: {'length': 2, 'dest': 37},
    0: {'length': 15, 'dest': 39}
}
get_dest_testdata = [
    (15, 0),  # same as key
    (52, 37), # same as key
    (23, 8),  # offset
    (13, 52), # offset
    (53, 38), # offset
    (54, 54), # not found, return source
    (60, 60)  # not found, return source
]
@pytest.mark.parametrize('test_input,expected', get_dest_testdata)
def test_get_dest(test_input, expected):
    assert get_dest(source=test_input, map=get_dest_testmap) == expected


# Solution tests

@pytest.mark.parametrize('test_input,expected', test_a, ids=["example"])
def test_solve_a(test_input, expected):
    assert str(solve_a(test_input)) == expected



# PART B

if p.answered_a:

    # Solution tests

    @pytest.mark.parametrize('test_input,expected', test_b, ids=["example"])
    def test_solve_b(test_input, expected):
        assert str(solve_b(test_input)) == expected