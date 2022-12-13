def populate_grid(input):
    global grid
    lines = input.splitlines()
    grid = [0] * len(lines)
    for i, line in enumerate(lines):
        grid[i] = list(line)
    return


def start_end() -> dict:
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            match char:
                case 'S':
                    start = [y, x]
                case 'E':
                    end = [y, x]
                case _:
                    continue
    coord = {
        'start': start,
        'end': end,
    }
    return coord


def elevation_change(frm: str, to: str) -> bool:
    diff = ord(to)-ord(frm)
    # print(f"from: {frm}, to: {to}, diff: {diff}")
    if diff <= 1:
        return True
    else:
        return False


def possible_moves(y: int, x: int) -> list:
    moves = set()
    elevation = grid[y][x]
    match elevation:
        case 'S':
            elevation = 'a'
        case 'E':
            elevation = 'z'
    if y >= 1:
        if elevation_change(elevation, grid[y-1][x]):
            moves.add('u')
    if x >= 1:
        if elevation_change(elevation, grid[y][x-1]):
            moves.add('l')
    try:
        if elevation_change(elevation, grid[y][x+1]):
            moves.add('r')
    except IndexError:
        pass
    try:
        if elevation_change(elevation, grid[y+1][x]):
            moves.add('d')
    except IndexError:
        pass
    # print(f"y: {y}, x: {x}, e: {elevation}, moves: {list(moves)}")
    return moves


def main():
    with open('input.txt') as f:
        input = f.read()
        populate_grid(input)
        print(possible_moves(0, 0))


if __name__ == '__main__':
    main()
