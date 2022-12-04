input_path = "AdventOfCode/2022/3.in"

rucksack = list()
with open(input_path, "r") as input:
    for line in input.readlines():
        rucksack.append(line.strip())

def priority(char):
    if char == char.lower():
        return ord(char) - 96
    else:
        return ord(char) - 38

letters = list()
for items in rucksack:
    size = int(len(items)/2)
    for char in items[:size]:
        if char in items[size:]:
            letters.append((items, char, priority(char)))
            break
    
print("Part 1: ", sum([x[2] for x in letters]))

badges = list()
for i in range(0, len(rucksack), 3):
    for char in rucksack[i]:
        if char in rucksack[i+1] and char in rucksack[i+2]:
            badges.append((char, priority(char)))
            break

print("Part 2: ", sum(x[1] for x in badges))
