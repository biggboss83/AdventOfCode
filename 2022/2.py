input_path = "2022/2.in"

points = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6,
    "A" : 1,
    "B" : 2,
    "C" : 3,
    ("A", "X") : 3,
    ("A", "Y") : 1,
    ("A", "Z") : 2,
    ("B", "X") : 1,
    ("B", "Y") : 2,
    ("B", "Z") : 3,
    ("C", "X") : 2,
    ("C", "Y") : 3,
    ("C", "Z") : 1
}

elves = dict()

with open(input_path, "r") as input:
    for line in input.readlines():
        (x, y) = line.strip().split()
        elves[(x,y)] = elves.get((x,y), 0) + points[y] + points[(x,y)]

print(sum(elves.values()))

