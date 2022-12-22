class Cycle:

    def __init__(self, cycle: int, register: int, sig: int, cmdline: str = None):
        self.cycle = cycle
        self.register = register
        self.sig = sig
        self.cmdline = cmdline

    def __repr__(self):
        return f"cycle: {self.cycle}, register: {self.register}, sig {self.sig}, cmdline: {self.cmdline}"

    def __str__(self):
        return f"cycle: {self.cycle}, register: {self.register}, sig {self.sig}, cmdline: {self.cmdline}"


def main(input):
    cycles = calc_sig_strength(input)
    sum = 0
    for i in [20, 60, 100, 140, 180, 220]:
        print(cycles[i-1])
        sum += cycles[i-1].sig
    return sum
    # 14680 - too high
    # 14678 - guess (based off 220th cmd), too high


def calc_sig_strength(input):
    print()
    x = 1
    c = 1
    cycles = []
    for line in input.splitlines():
        cmd = line.split()[0]
        if cmd == 'noop':
            num_cycles = 1
        else:
            num_cycles = 2

        for i in range(num_cycles):
            if cmd == 'addx':
                arg = int(line.split()[1])
                if i == 0:
                    cmdline = "({})".format(line)
                else:
                    cmdline = line
                    x += arg
            else:
                cmdline = line
            sig = c * x
            cycles.append(Cycle(c, x, sig, cmdline))
            print(cycles[-1])
            c += 1
    print()
    return cycles
    # currently returns the register value of one cycle AHEAD
    # i.e. cycle 220 should return what is currently returned by cycle 219
    # this exact error cause all but last test to fail

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(main(input))
