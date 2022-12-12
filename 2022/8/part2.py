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


def view_dist(tree_height, trees):
    # print()
    if len(trees) == 0:
        return 0
    for i, tree in enumerate(trees):
        # print(f"{i}: {tree}")
        if tree >= tree_height:
            break
    return i + 1


def scenic_val(y, x, input):
    # print()

    lines = input.splitlines()
    # print(lines)

    trees = populate_tress(lines)
    width = len(trees[0])
    height = len(trees)
    # print(trees)

    up = [trees[i][x] for i in range(y-1, -1, -1)]
    left = [trees[y][i] for i in range(x-1, -1, -1)]
    right = [trees[y][i] for i in range(x+1, width)]
    down = [trees[i][x] for i in range(y+1, height)]

    tree = trees[y][x]
    # print(f"y: {y}, x: {x}, tree: {tree}")
    up_dist = view_dist(tree, up)
    left_dist = view_dist(tree, left)
    right_dist = view_dist(tree, right)
    down_dist = view_dist(tree, down)

    # print(f"up:    {up} {up_dist}")
    # print(f"left:  {left} {left_dist}")
    # print(f"right: {right} {right_dist}")
    # print(f"down:  {down} {down_dist}")

    scenic = up_dist * left_dist * right_dist * down_dist
    # print(f"y: {y}, x: {x}, tree: {tree}, scenic: {scenic}")
    return scenic


def main():
    input = read_input('input.txt')
    lines = input.splitlines()  # ugly duplication
    # trees = populate_tress(lines)  # ugly duplication

    scenic_high = 0
    for y, line in enumerate(lines):
        for x, _ in enumerate(line):
            scenic = scenic_val(y, x, input)
            # print(f"y: {y}, x: {x}, scenic: {scenic}")
            if scenic > scenic_high:
                scenic_high = scenic
    print(scenic_high)

if __name__ == '__main__':
    main()
