import re
import math
import sys
import time
import gmpy2
# from gmpy2 import mpz

sys.set_int_max_str_digits(50000)


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
    rounds = 10000

    for r in range(1, rounds+1):
        # print("\n\n")
        # if r % 100 == 0:
        if r in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f"\nRound {r}\n-------------------------")
        for m, monkey in monkeys.items():
            # print(f"\n\nMonkey {m} ({monkey.operation})")
            for i in monkey.items:
                o = eval(monkey.operation, {"old": i})  # perform operation
                # b = math.floor(o // 3)  # get bored
                # if gmpy2.is_divisible(o, monkey.test_div):  # divisible?
                if divisible(o, monkey.test_div):  # divisible?
                    monkeys[monkey.test_true].items.append(o)
                    # print(f"Divisible by {monkey.test_div}, throw to {monkey.test_true}")
                else:
                    monkeys[monkey.test_false].items.append(o)
                    # print(f"Not divisible by {monkey.test_div}, throw to {monkey.test_false}")
                monkey.item_checks += 1
            monkey.items = []
        # print("\n")
        # if r % 100 == 0:
        if r in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            for m, monkey in monkeys.items():
                print(f"{m}: checks: {monkey.item_checks}")

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


def divisible(x: int, y: int) -> bool:

    match y:

        case 2:
            return int(str(x)[-1]) % 2 == 0

        # case 5:
        # https://www.k5learning.com/blog/math-divisibility-rules

        # case 7:
        # https://www.k5learning.com/blog/math-divisibility-rules

        case 9:
            return crosssum(x) == 9

        # case 11:

        case 13:
            return reduce_div(x, 13) % 13 == 0  # bad

        case 17:
            # return gmpy2.is_divisible(x, y)
            # return reduce17(x) % 17 == 0  # 1 ok, 20 bad
            return reduce_div(x, 17) % 17 == 0  # 1 ok, 20 bad

        case 18:  # This was a mistake - it isn't even necessary ¯\_(ツ)_/¯
            if divisible(x, 2):
                return divisible(x, 9)
            else:
                return False

        case 19:
            return reduce_div(x, 19) % 19 == 0 # bad

        case 23:
            return reduce_div(x, 23) % 23 == 0  # bad

        case _:
            if y % 2 == 0:  # if y is even, x should also be divisible by 2, which is a quick check
                if not divisible(x, 2):
                    return False
            else:
                return x % y == 0


def crosssum(x: int) -> int:
    y = x
    while True:
        y = sum([int(a) for a in str(y)])
        if y < 10:
            return y


def reduce_div(x: int, y: int) -> int:
    i = 1

    match y:
        case 13:
            digits = 1
            factor = 4

        case 17:
            digits = 1
            factor = 5

        case 19:
            digits = 2
            factor = 4

        case 23:
            digits = 1
            factor = 7

        case _:
            return None

    tic = time.perf_counter()
    while len(str(x)) > (digits + 1):
        a = int(str(x)[-digits:]) * factor  # multiply last digit(s)
        b = int(str(x)[:-digits])  # get remaining digits
        x = a + b  # if the sum of the numbers are divisible, so is the original number
        # print(f"{a=}, {b=}, {c=}")
        i += 1
    toc = time.perf_counter()
    # print(f"reduce {y} finished after {toc - tic:0.2f} seconds {i} iterations")
    return x


def calc(input):
    result = []

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(main(input))
