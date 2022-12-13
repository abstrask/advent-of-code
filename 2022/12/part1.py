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


def get_possible_moves(yx: list) -> list:
    y = yx[0]
    x = yx[1]
    moves = {}
    elevation = grid[y][x]
    match elevation:
        case 'S':
            elevation = 'a'
        case 'E':
            elevation = 'z'
    if y >= 1:
        if elevation_change(elevation, grid[y-1][x]):
            moves['u'] = [y-1, x]
    if x >= 1:
        if elevation_change(elevation, grid[y][x-1]):
            moves['l'] = [y, x-1]
    try:
        if elevation_change(elevation, grid[y][x+1]):
            moves['r'] = [y, x+1]
    except IndexError:
        pass
    try:
        if elevation_change(elevation, grid[y+1][x]):
            moves['d'] = [y+1, x]
    except IndexError:
        pass
    # print(f"y: {y}, x: {x}, e: {elevation}, moves: {list(moves)}")
    return moves


def move():
    here = start_end()['start']
    end = start_end()['end']
    trails = {}
    moves = 0
    while here != end:
        for move, coord in get_possible_moves(here).items():
            new_trail = trails[here] + move
            if len(new_trail) < len(trails[coord]):
                trails[coord] = new_trail

            print(trails[coord])
            here  # Something something... https://www.geeksforgeeks.org/a-search-algorithm/
            here = end  # debug
    return moves


def main():
    with open('input.txt') as f:
        input = f.read()
        populate_grid(input)
    move()


if __name__ == '__main__':
    main()
