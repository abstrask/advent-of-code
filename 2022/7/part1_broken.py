from dataclasses import dataclass


def read_input(file):
    with open(file) as f:
        return f.read()


def dir_rel_size(lines):
    path = []
    rel_size = {}
    for i, v in enumerate(lines):
        tokens = v.split()
        print(tokens)
        if tokens[0] == '$':
            print()
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
                name = tokens[1]
                if path_str in rel_size.keys():
                    rel_size[path_str] += size
                else:
                    rel_size[path_str] = size
                print(f"path: {path_str}, name: {name}, size: {size}, sum: {rel_size[path_str]}")
    return rel_size


def dir_tot_size(rel_size):
    tot_size = {}
    for path in rel_size.keys():
        for i, (k, v) in enumerate(rel_size.items()):
            if k.startswith(path):
                if path in tot_size.keys():
                    tot_size[path] += v
                else:
                    tot_size[path] = v
    return tot_size


def solve(input):
    lines = input.splitlines()
    rel_size = dir_rel_size(lines)
    # print(f"rel_size: {rel_size}")
    tot_size = dir_tot_size(rel_size)
    # print(f"tot_size: {tot_size}")

    # sum of dir size <= 100000
    result = 0
    for i, (k, v) in enumerate(tot_size.items()):
        if v <= 100000:
            # print(f"{k}, size: {v}")
            result += v
        # else:
        #     print(f"{k}, size: {v}")
    return result


def main():
    input = read_input('input.txt')
    print(solve(input))
    # 1.331.842 - too low


if __name__ == '__main__':
    main()
