# file_name = 'example'
file_name = 'input'

# Part One


def parse_stack_line(line):
    pos = 1
    item = 1
    items = {}
    while pos < len(line):
        if len(line[pos].strip()) > 0:
            items[item] = line[pos]
        item += 1
        pos += 4
    return items

def parse_instruction_line(line):
    elements = line.split(' ')
    instruction = {
        'ops': int(elements[1]),
        'from': int(elements[3]),
        'to': int(elements[5])
    }
    return instruction


with open(file_name) as f:
    lines = f.read().splitlines()

# Split input into stack description and instructions
stack_lines = []
instruction_lines = []
stack_description = True
for line in lines:
    if line == "":
        stack_description = False
        continue
    if stack_description:
        stack_lines.append(line)
    else:
        instruction_lines.append(line)
stack_lines.reverse()


# Populate stacks
stacks_one = {}
for line in stack_lines:
    # print(line)
    for i, (k, v) in enumerate(parse_stack_line(line).items()):
        if stacks_one.keys().__contains__(k):
            stacks_one[k].append(v)
        else:
            stacks_one[k] = [] # use key from parse_stack_lines, which is based solely on position. Could also use 'v', as the first line processed, contains the number/key of the stack.

print(f"\nStacks One: {stacks_one}\n")


# Process instructions
for line in instruction_lines:
    instruct = parse_instruction_line(line)
    print(instruct)
    op = 1
    while op <= instruct['ops']:
        crate = stacks_one[instruct['from']].pop()
        print(f"Moving crate {crate} from {instruct['from']} to {instruct['to']}")
        stacks_one[instruct['to']].append(crate)
        op += 1
    # print(f"{stacks_one}\n")


# Get result
part_one_list = []
for v in stacks_one.values():
    part_one_list += v[-1] # get last element of each stack
part_one = "".join(part_one_list)

print(f"\nPart One: {part_one}\n")
# JDTMRWCQJ


# Part Two


# Populate stacks
stacks_two = {}
for line in stack_lines:
    # print(line)
    for i, (k, v) in enumerate(parse_stack_line(line).items()):
        if stacks_two.keys().__contains__(k):
            stacks_two[k].append(v)
        else:
            stacks_two[k] = [] # use key from parse_stack_lines, which is based solely on position. Could also use 'v', as the first line processed, contains the number/key of the stack.

print(f"\nStacks Two: {stacks_two}\n")


# Process instructions
for line in instruction_lines:
    instruct = parse_instruction_line(line)
    print(instruct)
    op = 1
    crates = []
    while op <= instruct['ops']:
        crates += stacks_two[instruct['from']].pop()
        op += 1
    print(f"Moving {instruct['ops']} crates {crates} from {instruct['from']} to {instruct['to']}")
    crates.reverse()
    for crate in crates:
        stacks_two[instruct['to']].append(crate)
    # print(f"{stacks_two}\n")


# Get result
part_two_list = []
for v in stacks_two.values():
    part_two_list += v[-1] # get last element of each stack
part_two = "".join(part_two_list)


print(f"\nPart Two: {part_two}\n")
#