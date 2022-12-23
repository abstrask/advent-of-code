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
    crt_width = 40
    crt_height = 6
    crt_screen = ''
    for l in range(crt_height):
        crt_line = ''
        x = 0
        for p in range(crt_width):
            c = p + l * crt_width  # which cycle to lookup
            x = cycles[c].register
            # print(cycles[c])
            # print(l, p, c, x, abs(x-p))
            if abs(x-p) <= 1:
                crt_line += '#'
            else:
                crt_line += '.'
        # print(crt_line)
        crt_screen += f"""\
{crt_line}
"""
    # print(crt_screen)
    return crt_screen


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
            cmdline = line
            sig = c * x
            cycles.append(Cycle(c, x, sig, cmdline))
            # print(cycles[-1])
            if cmd == 'addx':
                if i == 0:
                    cmdline = "({})".format(line)
                else:
                    arg = int(line.split()[1])
                    x += arg
            c += 1
    return cycles

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(main(input))
