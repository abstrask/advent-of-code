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
    # print(lines)

    trees = populate_tress(lines)
    # print(trees)

    width = len(trees[0])
    height = len(trees)
    count_edge = (2 * width) + (2 * height) - 4

    # iterate over trees
    visible = 0
    for (y, row) in enumerate(trees):
        if y == 0 or y == height - 1:
            continue  # skip first and last row
        for (x, tree) in enumerate(row):
            if x == 0 or x == width - 1:
                continue  # skip first and last col
            # print(f"\n{y}, {x}: {tree}")

            left = trees[y][0:x]
            right = trees[y][x+1:width]
            # print(f"left: {left}, right: {right}")

            up = [trees[i][x] for i in range(0, y)]
            down = [trees[i][x] for i in range(y+1, height)]
            # print(f"up: {up}, down: {down}")

            if tree > max(left) or tree > max(right) or tree > max(up) or tree > max(down):
                visible += 1

    visible += count_edge
    return visible


def main():
    input = read_input('input.txt')
    print(solve(input))
    #


if __name__ == '__main__':
    main()
