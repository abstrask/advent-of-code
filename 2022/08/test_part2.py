import unittest
from parameterized import parameterized_class
import part2 as part

input = '''\
30373
25512
65332
33549
35390
'''


@parameterized_class(('height', 'trees', 'expected'), [
    (5, [3], 1),  # A up
    (5, [5, 2], 1),  # A left
    (5, [1, 2], 2),  # A right
    (5, [3, 5, 3], 2),  # A down
    (5, [3, 5, 3], 2),  # B up
    (5, [3, 3], 2),  # B left
    (5, [4, 9], 2),  # B right
    (5, [3], 1),  # B down
])
class TestViewDistance(unittest.TestCase):
    def test_view_dist(self):
        self.assertEqual(part.view_dist(self.height, self.trees), self.expected)


@parameterized_class(('y', 'x', 'expected'), [
    (1, 2, 4),  # A
    (3, 2, 8),  # B
])
class TestScenicValue(unittest.TestCase):
    def test_scenic(self):
        self.assertEqual(part.scenic_val(self.y, self.x, input), self.expected)


if __name__ == '__main__':
    unittest.main()
