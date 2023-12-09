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

calc_a_testdata = [
    ('32T3K', 20302100313),
    ('T55J5', 41005051105),
    ('KK677', 31313060707),
    ('KTJJT', 31310111110),
    ('QQQJA', 41212121114),
]
@pytest.mark.parametrize('test_input,expected', calc_a_testdata)
def test_calc_a(test_input, expected):
    assert calc_a(test_input) == expected


# Solution tests

@pytest.mark.parametrize('test_input,expected', test_a, ids=["example"])
def test_solve_a(test_input, expected):
    assert str(solve_a(test_input)) == expected


# PART B

if p.answered_a:

    # Intermediate tests

    calc_b_testdata = [
        ('32T3K', 20302100313),
        ('T55J5', 61005050105),
        ('KK677', 31313060707),
        ('KTJJT', 61310010110),
        ('QQQJA', 61212120114),
        ('33377', 50303030707), # full house
        ('4JJJ8', 60401010108), # four of a kind with joker
        ('2233A', 30202030314) # 2 pairs
    ]
    @pytest.mark.parametrize('test_input,expected', calc_b_testdata)
    def test_calc_b(test_input, expected):
        assert calc_b(test_input) == expected


    # Solution tests

    # @pytest.mark.parametrize('test_input,expected', test_b, ids=["example"])
    # def test_solve_b(test_input, expected):
    #     assert str(solve_b(test_input)) == expected

    # EXAMPLE NOT UPDATED!
    example_b = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    def test_solve_b():
        assert solve_b(example_b) == 5905