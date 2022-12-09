import unittest
# from parameterized import parameterized, parameterized_class
from parameterized import parameterized_class
import part1 as part


@parameterized_class(('input', 'expected'), [
    ('''\
30373
25512
65332
33549
35390
''', 21),
])
class TestStringMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(part.solve(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
