import numpy as np

input_path = "2022/8.in"

with open(input_path, "r") as input:
    trees = [list(map(int, line.strip())) for line in input.readlines()]
    forest = np.array(trees, dtype=int, ndmin=2)

visible = np.zeros(forest.shape, dtype=int)

def visibility(forest, transposed=False):
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            x, y = (j, i) if transposed else (i, j)
            if visible[x][y]:
                continue
            elif tree > max(row[:j], default=-1) or tree > max(row[j+1:], default=-1):
                visible[x][y] = 1

visibility(forest)
visibility(forest.T, True)
print("Part A: ", visible.sum())


scores = np.zeros(forest.shape, dtype=int)

def scenic(forest):
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            left = scenic_length(tree, np.flip(row[:j+1]))
            up = scenic_length(tree, np.flip(forest[:i+1,j]))
            right = scenic_length(tree, row[j:])
            down = scenic_length(tree, forest[i:,j])
            scores[i][j] = left * up * right * down
            

def scenic_length(tree, row):
    if len(row) == 1:
        return 0
    elif tree <= row[1]:
        return 1
    else:
        return 1 + scenic_length(tree, row[1:])

scenic(forest)
print("Part B:", scores.max())