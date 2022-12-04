input_path = "AdventOfCode/2021/25.in"

with open(input_path, "r") as input:
    seabed = [x.strip() for x in input.readlines()]

E = ">"
S = "v"
O = "."

def step(row, dir):
    temp = row[-1] + row + row[0]
    temp = temp.replace(dir+O, O+dir)
    return temp[1:-1]

def transpose(table):
    return [''.join(row) for row in zip(*table)]


moving = True
count = 0
while moving:
    moving_east = False
    moving_south = False
    for i, row in enumerate(seabed):
        seabed[i] = step(row, E)
        moving_east = moving_east or row != seabed[i]
    seabed = transpose(seabed)
    for j, col in enumerate(seabed):
        seabed[j] = step(col, S)
        moving_south = moving_south or col != seabed[j]
    seabed = transpose(seabed)
    moving = moving_east or moving_south
    count += 1

print(count)