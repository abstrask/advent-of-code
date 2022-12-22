import unittest
from parameterized import parameterized_class
import part1 as part

input1 = '''\
noop
addx 3
addx -5
'''

input2 = '''\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''


# print(part.main(input2))


@parameterized_class(('input', 'expected'), [
    (input1, -1),
    # (input2, 13140),
])
class TestLastSigStrength(unittest.TestCase):
    def test_last_sig_strength(self):
        self.assertEqual(part.calc_sig_strength(self.input)[-1].register, self.expected)


@parameterized_class(('input', 'cycle', 'expected'), [
    # (input1, 1),
    (input2, 20, 420),
    (input2, 60, 1140),
    (input2, 100, 1800),
    (input2, 140, 2940),
    (input2, 180, 2880),
    (input2, 220, 4180),
])
class TestCycleSigStrength(unittest.TestCase):
    def test_cycle_sig_strength(self):
        self.assertEqual(part.calc_sig_strength(self.input)[self.cycle-1].sig, self.expected)


@parameterized_class(('input', 'expected'), [
    # (input1, 1),
    (input2, 13140),
])
class TestSumSigStrength(unittest.TestCase):
    def test_sum_sig_strength(self):
        self.assertEqual(part.main(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
