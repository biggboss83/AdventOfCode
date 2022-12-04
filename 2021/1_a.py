input = open("AdventOfCode/2021/1_input.txt", "r")

current = int(input.readline())
count = 0
for x in input:
    if int(x) > current:
        count += 1
    current = int(x)

print(count)

input.close()