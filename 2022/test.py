input_path = "AdventOfCode/2021/25test.in"

with open(input_path, "r") as input:
    seabed = [list(x.strip()) for x in input.readlines()]

E = ">"
S = "v"
O = "."

def step(row, dir):
    print("1: ", row)
    moving = False
    for i, cell in enumerate(row):
        if cell != dir:
            continue
        next_cell = (i+1) % len(row)
        if row[next_cell] == O:
            row[i] = O + O
            row[next_cell] = dir + dir
            moving = True
    for i, cell in enumerate(row):
        if cell == O + O:
            row[i] = O
        if cell == dir + dir:
            row[i] = dir
    print("2: ", row)
    return moving

def transpose(table):
    return [list(row) for row in zip(*table)]

def print_seabed():
    for row in seabed:
        print(''.join(row))


moving = True
count = 0
while moving:
    moving_east = False
    moving_south = False
    for row in seabed:
        moving_east = moving_east or step(row, E)
    seabed = transpose(seabed)
    for col in seabed:
        moving_south = moving_south or step(col, S)
    seabed = transpose(seabed)
    count += 1
    print(count)
    print_seabed()
    if count == 1:
        break
    moving = moving_east or moving_south



print(count)