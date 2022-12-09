import os.path

def read_input(file):
    with open(file) as f:
        return f.read()


def get_dir_size(lines):
    dir_size = {}
    for i, v in enumerate(lines):
        tokens = v.split()
        # print(tokens)
        if tokens[0] == '$':
            # print()
            cmd = tokens[1]
            if cmd == 'cd':
                rel_dir = tokens[2]
                if rel_dir == '/':
                    pwd = '/'
                elif rel_dir == '..':
                    pwd = os.path.dirname(pwd) or '/'
                else:
                    pwd = os.path.join(pwd, rel_dir)
                if pwd not in dir_size.keys():
                    dir_size[pwd] = 0
                # print(pwd)
        else:
            if not tokens[0] == 'dir':
                file = os.path.join(pwd, tokens[1])
                size = int(tokens[0])
                # print(f"file: {file}, size: {size}")
                dir_size[pwd] += size
    return dir_size


def get_dir_tot_size(dir_size):
    tot_size = {}
    for path in dir_size.keys():
        for i, (k, v) in enumerate(dir_size.items()):
            if k.startswith(path):
                if path in tot_size.keys():
                    tot_size[path] += v
                else:
                    tot_size[path] = v
    return tot_size


def solve(input):
    print()
    lines = input.splitlines()
    dir_size = get_dir_size(lines)
    # print(f"dir_size: {dir_size}")
    tot_size = get_dir_tot_size(dir_size)
    print(f"tot_size: {tot_size}")
    # tot_size_sorted = sorted(tot_size.items(), key=lambda x: x[1], reverse=True)
    sizes_sorted = sorted(tot_size.values())

    capacity = 70000000
    need = 30000000
    used = tot_size['/']
    free = capacity - used

    for dir_size in sizes_sorted:
        if dir_size > (need - free):
            return dir_size
    return 0


def main():
    input = read_input('input.txt')
    print(solve(input))
    #


if __name__ == '__main__':
    main()
