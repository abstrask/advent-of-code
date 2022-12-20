import unittest
# from parameterized import parameterized, parameterized_class
from parameterized import parameterized_class
import part2 as part


@parameterized_class(('input', 'expected'), [
    ('''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
''', 24933642),
])
class TestStringMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(part.solve(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
