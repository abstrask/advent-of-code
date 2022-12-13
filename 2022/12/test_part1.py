import unittest
from parameterized import parameterized_class
import part1 as part

input = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
part.populate_grid(input)

test_start_end = {
    'start': [0, 0],
    'end': [2, 5],
}


class TestFindCoord(unittest.TestCase):
    def test_start_end(self):
        self.assertDictEqual(part.start_end(), test_start_end)


@parameterized_class(('frm', 'to', 'expected'), [
    ('a', 'a', True),
    ('a', 'b', True),
    ('a', 'c', False),
    ('a', 'z', False),
    ('z', 'a', True),
    ('b', 'a', True),
    ('c', 'a', True),
])
class TestElevationChange(unittest.TestCase):
    def test_elevation_change(self):
        self.assertEqual(part.elevation_change(self.frm, self.to), self.expected)


@parameterized_class(('y', 'x', 'expected'), [
    (0, 0, {'d', 'r'}),  # wraps around array?!
    (1, 7, {'u', 'd'}),
    (4, 3, {'l', 'r'}),
    (4, 7, {'l', 'u'}),
])
class TestPossibleMoves(unittest.TestCase):
    def test_possible_moves(self):
        self.assertSetEqual(part.possible_moves(self.y, self.x), self.expected)


# known locs(?)
# [x,y] min_moves


if __name__ == '__main__':
    unittest.main()
