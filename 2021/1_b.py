input = open("AdventOfCode/2021/1_input.txt", "r")

x = list(input)

for i in range(len(x)-3):
    print(x[0], len(x))

input.close()