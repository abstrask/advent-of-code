import os.path


def read_input(file):
    with open(file) as f:
        return f.read()


def populate_tress(lines):
    trees = [0] * len(lines)
    for i, line in enumerate(lines):
        # print(f"{i}: {line}")
        trees[i] = list(line)
    return trees


def solve(input):
    print()

    lines = input.splitlines()
    print(lines)

    trees = populate_tress(lines)

    w = len(trees[0])
    h = len(trees)

    # ...


def main():
    input = read_input('input.txt')
    print(solve(input))
    #


if __name__ == '__main__':
    main()
