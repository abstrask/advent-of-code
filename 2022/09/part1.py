from sys import exit


def main(input):
    global head, tail
    head = [[0, 0]]
    tail = [[0, 0]]
    for line in input.splitlines():
        # print()
        direction, moves = line.split()
        move_head(direction, int(moves))
    tail_pos = []
    for pos in tail:
        tail_pos.append("%s,%s" % (pos[0], pos[1]))
    return len(set(tail_pos))


def sign(number: int):
    match number:
        case _ if number > 0:
            return 1
        case _ if number < 0:
            return -1
        case _ if number == 0:
            return 0


def move_head(direction: str, moves: int):
    # print(direction, moves)
    last = head[-1]
    x = last[0]
    y = last[1]
    for _ in range(moves):
        match direction:
            case 'U':
                y += 1
            case 'L':
                x -= 1
            case 'R':
                x += 1
            case 'D':
                y -= 1
            case _:
                exit(1)
        head.append([x, y])
        move_tail(x, y)
    return


def move_tail(x_head: int, y_head: int):
    last = tail[-1]
    x = last[0]
    y = last[1]
    x_diff = x_head - x
    y_diff = y_head - y
    # print(f"Tail: {x}, {y}")
    # print(f"Head: {x_head}, {y_head}")
    # print(f"Diff: {x_diff}, {y_diff}")
    if max([abs(x_diff), abs(y_diff)]) > 1:
        x += sign(x_diff)
        y += sign(y_diff)
        # print(f"New:  {x}, {y}")
        tail.append([x, y])
    return


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(main(input))
