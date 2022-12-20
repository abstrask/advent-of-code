import unittest
# from parameterized import parameterized, parameterized_class
from parameterized import parameterized_class
import part1 as part


@parameterized_class(('input', 'expected'), [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
])
class TestStringMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(part.solve(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
