import unittest
from parameterized import parameterized_class
import part1 as part

input = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''


class TestMostActiveProduct(unittest.TestCase):
    def test_most_active_product(self):
        self.assertEqual(part.main(input), 10605)


# @parameterized_class(('input', 'cycle', 'expected'), [
#     (input2, 20, 420),
#     (input2, 60, 1140),
#     (input2, 100, 1800),
#     (input2, 140, 2940),
#     (input2, 180, 2880),
#     (input2, 220, 3960),
# ])
# class TestCycleSigStrength(unittest.TestCase):
#     def test_cycle_sig_strength(self):
#         self.assertEqual(part.calc_sig_strength(self.input)[self.cycle-1].sig, self.expected)


# @parameterized_class(('input', 'expected'), [
#     (input2, 13140),
# ])
# class TestSumSigStrength(unittest.TestCase):
#     def test_sum_sig_strength(self):
#         self.assertEqual(part.main(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
