input_path = "AdventOfCode/2022/4.in"

sections = list()
with open(input_path, "r") as input:
    subsets = 0
    overlaps = 0
    for line in input.readlines():
        line = line.strip().replace('-',',').split(',')
        sections.append(list(map(int, line)))
    for pair in sections:
        first = set(range(pair[0], pair[1]+1))
        second = set(range(pair[2], pair[3]+1))
        if first.issubset(second) or second.issubset(first):
            subsets +=1
        if first.intersection(second) != set():
            overlaps +=1

print("Part 1: ", subsets)
print("Part 2: ", overlaps)

