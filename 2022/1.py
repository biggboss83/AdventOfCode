input_path = "2022/1.in"

elves = list()

with open(input_path, "r") as input:
    elf = list()
    for line in input.readlines():
        temp = line.strip()
        if not temp:
            elves.append(elf)
            elf = list()
        else:
            elf.append(int(temp))
    elves.append(elf)
        
sums = [sum(elf) for elf in elves]
print(max(sums))
top_three = sorted(sums, reverse=True)[:3]
print(sum(top_three))
