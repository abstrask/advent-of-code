def read_input(file):
    with open(file) as f:
        return f.read().splitlines()


def solve(line):
    distinct_chars = 4
    for i, v in enumerate(line):
        if i < distinct_chars - 1:
            continue
        is_marker = True
        start_slice = i + 1 - distinct_chars
        end_slice = i + 1
        marker = line[start_slice:end_slice]
        # print(f"\n{i+1}: {marker}")
        for c in marker:
            # print(f"{c}: {marker.count(c)}")
            if marker.count(c) > 1:
                is_marker = False
                break
        if is_marker:
            return i + 1
    return 1


def main():
    for line in read_input('input'):
        print(solve(line))


if __name__ == '__main__':
    main()
