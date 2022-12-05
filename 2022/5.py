input_path = "2022/5.in"

crates = dict()
moves = list()

def transpose(table):
    return [''.join(row) for row in zip(*table)]

with open(input_path, "r") as input:
    temp = list()
    for line in input:
        if not line.strip():
            break
        temp.append(line.replace('\n', ''))
    for line in input:
        moves.append(line.strip())
    ids = list(map(int, temp.pop().split()))
    for id in ids:
        crates[id] = []
    for t in temp:
        for id, el in enumerate(range(1, len(t), 4)):
            if t[el].isalpha():
                crates[id+1].insert(0, t[el])

# Part A
"""
for move in moves:
    move = move.split()
    for i in range(int(move[1])):
        crates[int(move[5])].append(crates[int(move[3])].pop())
"""

# Part B
print(crates)
for move in moves:
    move = move.split()
    crate_from = crates[int(move[3])]
    crate_to = crates[int(move[5])]
    qty = int(move[1])
    crate_to.extend(crate_from[-qty:])
    del crate_from[-qty:]

tops = list()
for key in crates.keys():
    tops.append(crates[key].pop())
tops = ''.join(tops)

print(tops)
