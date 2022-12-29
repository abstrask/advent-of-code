import re
import math


class Monkey:

    def __init__(self, items: list[int], operation: str, test_div: int, test_true: int, test_false: int, item_checks: int):
        self.items = items
        self.operation = operation
        self.test_div = test_div
        self.test_true = test_true
        self.test_false = test_false
        self.item_checks = item_checks

    def __repr__(self):
        return f"items: {self.items},operation: {self.operation}, test_div {self.test_div}, test_true: {self.test_true}, test_false: {self.test_false}, item_checks: {self.item_checks}"
        # return f"{self.items=}, {self.operation=}, {self.test_div=}, {self.test_true=}, {self.test_false=}, {self.item_checks=}"

    def __str__(self):
        return f"items: {self.items},operation: {self.operation}, test_div {self.test_div}, test_true: {self.test_true}, test_false: {self.test_false}, item_checks: {self.item_checks}"


def main(input):
    monkeys = init(input)
    rounds = 20

    for r in range(1, rounds+1):
        # print("\n\n")
        print(f"\nRound {r}\n-------------------------")
        for m, monkey in monkeys.items():
            # print(f"\n\nMonkey {m} ({monkey.operation})")
            for i in monkey.items:
                o = eval(monkey.operation, {"old": i})  # perform operation
                b = math.floor(o / 3)  # get bored
                # print(f"\n{i} -> {o} -> {b}")
                if b % monkey.test_div == 0:  # divisible?
                    monkeys[monkey.test_true].items.append(b)
                    # print(f"Divisible by {monkey.test_div}, throw to {monkey.test_true}")
                else:
                    monkeys[monkey.test_false].items.append(b)
                    # print(f"Not divisible by {monkey.test_div}, throw to {monkey.test_false}")
                monkey.item_checks += 1
            monkey.items = []
        # print("\n")
        for m, monkey in monkeys.items():
            # print(f"{m}: {monkey}")
            print(f"{m}: {monkey.items}, checks: {monkey.item_checks}")
            pass

    # Most active monkeys
    item_checks = sorted([(v).item_checks for v in monkeys.values()], reverse=True)
    result = item_checks[0] * item_checks[1]
    return result


def init(input):
    monkeys = {}
    for line in input.splitlines():
        if line.startswith("Monkey "):
            match = re.search("^Monkey (\d+):$", line)
            monkey = int(match.group(1))
        if line.startswith("  Starting items: "):
            match = re.search("^.*: (.*)$", line)
            items = [int(i) for i in match.group(1).split(", ")]
        if line.startswith("  Operation: "):
            operation = line.split(" = ")[1]
        if line.startswith("  Test: "):
            test_div = int(line.split(" by ")[1])
        if line.startswith("    If true: "):
            test_true = int(line.split(" monkey ")[1])
        if line.startswith("    If false: "):
            test_false = int(line.split(" monkey ")[1])
            monkeys[monkey] = Monkey(items, operation, test_div, test_true, test_false, 0)
    # print(monkeys)
    return monkeys


def calc(input):
    result = []

    return result

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(main(input))
