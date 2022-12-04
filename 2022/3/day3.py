# file_name = 'example.txt'
file_name = 'input.txt'

# Part One

with open(file_name) as f:
    lines = f.read().splitlines()

prio_sum = 0

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
            prio_sum += prio
            break

print(prio_sum)

# Answer: 7763


## Part Two

