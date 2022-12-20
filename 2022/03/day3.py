# file_name = 'example.txt'
file_name = 'input.txt'

# Part One

with open(file_name) as f:
    lines = f.read().splitlines()

one_sum = 0

for line in lines:
    split = int(line.__len__() / 2)
    first = line[:split]
    second = line[split:]
    for char in first:
        if char in second:
            if char.isupper():
                prio = ord(char) - 38
            else:
                prio = ord(char) - 96
            print(f"{char}: {prio}")
            one_sum += prio
            break

print(f"Part One: {one_sum}\n")

# Answer: 7763


## Part Two

two_sum = 0

i = 0
while(i < len(lines)):
    group = lines[i:i+3]
    # print(group)
    for char in group[0]:
        if (char in group[1] and char in group[2]):
            if char.isupper():
                prio = ord(char) - 38
            else:
                prio = ord(char) - 96
            print(f"{char}: {prio}")
            two_sum += prio
            break
    i += 3

print(f"Part Two: {two_sum}\n")