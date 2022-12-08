from dataclasses import dataclass


def read_input(file):
    with open(file) as f:
        return f.read()

def dir_rel_size():


def solve(input):


    lines = input.splitlines()

    path = []
    dir_size = {}
    for i, v in enumerate(lines):
        tokens = v.split()
        print(tokens)
        if tokens[0] == '$':
            cmd = tokens[1]
            if cmd == 'cd':
                rel_dir = tokens[2]
                if rel_dir == '/':
                    path = []
                elif rel_dir == '..':
                    path.pop()
                else:
                    path.append(tokens[2])
                print(f"path: {path}")
            if cmd == 'ls':
                continue  # any line not changing directory, is an ls output
        else:
            if not tokens[0] == 'dir':
                path_str = "/%s" % '/'.join(path)
                size = int(tokens[0])
                print(path_str)
                if path_str in dir_size.keys():
                    dir_size[path_str] += size
                else:
                    dir_size[path_str] = size
    print(dir_size)
    return 1


def main():
    input = read_input('input.txt')
    print(solve(input))


if __name__ == '__main__':
    main()
