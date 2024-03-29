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



# PART A

# Intermediate tests

# calc_a_testdata = [
#     ('0', 0)
# ]
# @pytest.mark.parametrize('test_input,expected', calc_a_testdata)
# def test_calc_a(test_input, expected):
#     assert calc_a(test_input) == expected


# Solution tests

example_a = [
    ('''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)''', 2),
    ('''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)''', 6),
]
@pytest.mark.parametrize('test_input,expected', example_a)
def test_solve_a(test_input, expected):
    assert solve_a(test_input) == expected


# @pytest.mark.parametrize('test_input,expected', test_a, ids=["example"])
# def test_solve_a(test_input, expected):
#     assert str(solve_a(test_input)) == expected # example answer parsed wrong


# PART B

if p.answered_a:

    # Intermediate tests

    # calc_b_testdata = [
    #     ('0', 0)
    # ]
    # @pytest.mark.parametrize('test_input,expected', calc_b_testdata)
    # def test_calc_b(test_input, expected):
    #     assert calc_b(test_input) == expected


    # Solution tests

    # @pytest.mark.parametrize('test_input,expected', test_b, ids=["example"])
    # def test_solve_b(test_input, expected):
    #     assert str(solve_b(test_input)) == expected

    # EXAMPLE NOT UPDATED!
    example_b = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    def test_solve_b():
        assert solve_b(example_b) == 6