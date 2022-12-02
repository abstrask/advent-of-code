# file_name = 'example.txt'
file_name = 'input.txt'


# Part One

with open(file_name) as f:
    lines = f.read().splitlines()

cals = {}
elf = 1

count = 1
for line in lines:
    if line == '':
        elf += 1
    else:
        try:
            cals[elf] += int(line)
        except KeyError:
            cals[elf] = int(line)
    count += 1


print(f"Elfs:\n{cals}")

most_elf = max(cals, key=cals.get)
most_cals = max(cals, key=cals.get)

print(f"Carries most:\n{most_elf} = {cals[most_elf]}\n")

# Answer: 69693


# Part Two

most_elfs = sorted(cals, key=cals.get, reverse=True)
top3_elfs = most_elfs[0:3]

top3_cals = 0
for elf in top3_elfs:
    print(cals[elf])
    top3_cals += cals[elf]

print(f"Top 3 total cals: {top3_cals}")
