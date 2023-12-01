import unittest
from parameterized import parameterized_class
import part2 as part

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


# part.main(input)


# class TestMostActiveProduct(unittest.TestCase):
#     def test_most_active_product(self):
#         self.assertEqual(part.main(input), 10605)


@parameterized_class(('input', 'expected'), [
    (123456789, 9),
    (123456789012, 3),
])
class TestCrossSum(unittest.TestCase):
    def test_cross_sum(self):
        self.assertEqual(part.crosssum(self.input), self.expected)


@parameterized_class(('input', 'expected'), [
    (pow(13, 5), True),
    (pow(13, 5) + 3, False),
])
class TestReduce13(unittest.TestCase):
    def test_reduce_13(self):
        self.assertEqual(part.reduce_div(self.input, 13) % 13 == 0, self.expected)


@parameterized_class(('input', 'expected'), [
    (pow(17, 5), True),
    (pow(17, 5) + 3, False),
])
class TestReduce17(unittest.TestCase):
    def test_reduce_17(self):
        self.assertEqual(part.reduce_div(self.input, 17) % 17 == 0, self.expected)


@parameterized_class(('input', 'expected'), [
    (pow(19, 5), True),
    (pow(19, 5) + 3, False),
])
class TestReduce19(unittest.TestCase):
    def test_reduce_19(self):
        self.assertEqual(part.reduce_div(self.input, 19) % 19 == 0, self.expected)


@parameterized_class(('input', 'expected'), [
    (pow(23, 5), True),
    (pow(23, 5) + 3, False),
])
class TestReduce23(unittest.TestCase):
    def test_reduce_23(self):
        self.assertEqual(part.reduce_div(self.input, 23) % 23 == 0, self.expected)


# @parameterized_class(('input', 'expected'), [
#     (input2, 13140),
# ])
# class TestSumSigStrength(unittest.TestCase):
#     def test_sum_sig_strength(self):
#         self.assertEqual(part.main(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()