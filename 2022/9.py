import numpy as np

input_path = "2022/9.in"

visited = set((0,0))
DIR = {
    'U': np.array([1,0]),
    'R': np.array([0,1]),
    'D': np.array([-1,0]),
    'L': np.array([0,-1])
}


def distance(next, knot):
    return np.max(np.abs(next - knot))

def direction(next, knot):
    return (next - knot) // np.abs(next - knot)

def move_head(knot, dir):
    knot += dir

def move_tail(knot, next):
    if distance(knot, next) > 1:
        knot += direction(next, knot)
        visited.add(tuple(knot))

def move_knot(knot, next):
    if distance(knot, next) > 1:
        knot += direction(next, knot)

def move_rope(rope, dir):
    for i, knot in enumerate(rope):
        if i == 0:
            move_head(head, dir)
        elif i == len(rope) - 1:
            move_tail(knot, rope[i-1])
        else:
            move_knot(knot, rope[i-1])

rope = np.array([[0,0]] * 2)
head = rope[0]
tail = rope[-1]

with open(input_path, "r") as input:

    moves = [line.strip().split() for line in input.readlines()]
    for move in moves:
        dir, num = move
        for _ in range(int(num)):
            move_rope(rope, DIR[dir])
    print("Part A: ", len(visited))
    rope = np.array([[0,0]] * 10)
    visited = set((0,0))
    head = rope[0]
    tail = rope[-1]
    for move in moves:
        dir, num = move
        for _ in range(int(num)):
            move_rope(rope, DIR[dir])
    print("Part B: ", len(visited))