# file_name = 'example.txt'
file_name = 'input.txt'

# Part One

def get_min_max(input):
    range_input = input.split('-')
    return {
        'min': int(range_input[0]),
        'max': int(range_input[1])
    }

with open(file_name) as f:
    lines = f.read().splitlines()


part_one = 0

for line in lines:
    pairs = line.split(',')
    pair0 = get_min_max(pairs[0])
    pair1 = get_min_max(pairs[1])
    if (pair0['min'] <= pair1['min'] and pair0['max'] >= pair1['max']):
        print(pairs)
        part_one += 1
    elif (pair0['min'] >= pair1['min'] and pair0['max'] <= pair1['max']):
        print(pairs)
        part_one += 1

print(f"\nPart One: {part_one}\n")
# 538


## Part Two


part_two = 0

for line in lines:
    pairs = line.split(',')
    pair0 = get_min_max(pairs[0])
    pair1 = get_min_max(pairs[1])
    print(pairs)
    if pair0['min'] >= pair1['min'] and pair0['min'] <= pair1['max']:
        # print("contained A")
        # print(pairs)
        part_two += 1
    elif pair1['min'] >= pair0['min'] and pair1['min'] <= pair0['max']:
        # print("contained B")
        # print(pairs)
        part_two += 1
    print()

print(f"\nPart Two: {part_two}\n")
# 792