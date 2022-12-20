import unittest
# from parameterized import parameterized, parameterized_class
from parameterized import parameterized_class
import part2 as part


@parameterized_class(('input', 'expected'), [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
])
class TestStringMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(part.solve(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
