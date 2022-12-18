import unittest
from parameterized import parameterized_class
import part1 as part

input = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''


class TestNumVisits(unittest.TestCase):
    def test_num_visits(self):
        self.assertEqual(part.main(input), 13)


if __name__ == '__main__':
    unittest.main()