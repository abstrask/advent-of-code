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



expected_galaxies = {1: (0, 4), 2: (1, 9), 3: (2, 0), 4: (5, 8), 5: (6, 1), 6: (7, 12), 7: (10, 9), 8: (11, 0), 9: (11, 5)}


# PART A

# Intermediate tests

# @pytest.mark.parametrize('test_input,expected', test_a, ids=['galaxies'])
# def test_get_galaxies(test_input, expected):
#     assert get_galaxies(test_input) == expected_galaxies


def test_calc_a():
    assert calc_a(test_a[0][0]) == expected_galaxies


# Solution tests

@pytest.mark.parametrize('test_input,expected', test_a, ids=["example"])
def test_solve_a(test_input, expected):
    assert str(solve_a(test_input)) == expected


# PART B

if p.answered_a:

    # Intermediate tests

    # calc_b_testdata = [
    #     ('0', 0)
    # ]
    # @pytest.mark.parametrize('test_input,expected', calc_b_testdata)
    # def test_calc_b(test_input, expected):
    #     assert calc_b(test_input) == expected

    # def test_calc_b():
    #     assert calc_b(test_a[0][0]) == expected_galaxies


    # Solution tests

    solve_b_testdata = [
        (2, 374),
        (10, 1030),
        (100, 8410)
    ]
    @pytest.mark.parametrize('penalty,expected', solve_b_testdata)
    def test_solve_b(penalty, expected):
        assert solve_b(test_a[0][0], penalty) == expected

    # EXAMPLE NOT UPDATED!
    # example_b = """0
    # 0
    # 0"""
    # def test_solve_b():
    #     assert solve_b(example_b) == 0