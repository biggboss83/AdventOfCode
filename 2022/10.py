import numpy as np

input_path = "2022/10.in"

CPU = {
    0: 1
}

cycles = list(range(20, 221, 40))

with open(input_path, "r") as input:
    program = [line.strip().split() for line in input.readlines()]
    cycle = 1
    for line in program:
        if line[0] == "noop":
            CPU[cycle] = CPU[cycle] if cycle in CPU else CPU[cycle-1]
            cycle += 1
        elif line[0] == "addx":
            CPU[cycle] = CPU[cycle] if cycle in CPU else CPU[cycle-1]
            cycle += 1
            CPU[cycle] = CPU[cycle] if cycle in CPU else CPU[cycle-1]
            cycle += 1
            CPU[cycle] = CPU[cycle-1] + int(line[1])

print("Part A: ", sum([x * CPU[x] for x in cycles]))

HEIGHT = 6
WIDTH = 40
print("Part B:")

s = ''
for cycle in range(1, 241):
    if (cycle - 1) % 40 == 0:
        print(s)
        s = ''
    sprite = [max(CPU[cycle] - 1, 1), CPU[cycle], min(CPU[cycle] + 1, 240)]
    if (cycle - 1) % 40 in sprite:
        s += '#'
    else:
        s += ' '
print(s)