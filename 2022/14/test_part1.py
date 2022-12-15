import unittest
from parameterized import parameterized_class
import part1 as part

input = '''\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''

# print(input)
part.init(input)

# print(input[0])

# print(part.commands)
# print(part.bounds)
# part.populate_rocks()

if __name__ == '__main__':
    unittest.main()