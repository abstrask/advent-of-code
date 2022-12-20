import unittest
from parameterized import parameterized_class
import part2 as part

input1 = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

input2 = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''


@parameterized_class(('input', 'expected'), [
    (input1, 1),
    # (input2, 36),
])
class TestNumVisits(unittest.TestCase):
    def test_num_visits(self):
        self.assertEqual(part.main(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
