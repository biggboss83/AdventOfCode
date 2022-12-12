import numpy as np

input_path = "2022/12.in"

def adjacent(coord, max_row, max_col):
    row, col = coord
    up = (row - 1, col) if row > 0 else None
    right = (row, col + 1) if col < max_col - 1 else None
    down = (row + 1, col) if row < max_row - 1 else None
    left = (row, col - 1) if col > 0 else None
    return [dir for dir in [up, right, down, left] if dir]

def height(cell):
    if cell == 'S':
        return ord('a')
    elif cell == 'E':
        return ord('z')
    else:
        return ord(cell)

def neighbours(heightmap, cell):
    max_row, max_col = heightmap.shape
    cell_height = height(heightmap[cell[0]][cell[1]])
    adjacent_cells = adjacent(cell, max_row, max_col)
    return[x for x in adjacent_cells if height(heightmap[x[0]][x[1]]) <= cell_height + 1]


visited = dict()
queue = []
PART_A = True
with open(input_path, "r") as input:
    heightmap = np.array([list(line.strip()) for line in input.readlines()])
    HEIGHT, WIDTH = len(heightmap), len(heightmap[0])
    start_cell = 'S' if PART_A else 'a'
    start = [tuple(x) for x in np.argwhere(heightmap == start_cell)]
    end = tuple(*np.argwhere(heightmap == 'E'))
    queue.append(start)
    for cell in start:
        visited[cell] = 0

    not_found = True
    while not_found:
        level = queue.pop()
        next_level = []
        for cell in level:
            for neighbour in neighbours(heightmap, cell):
                if neighbour not in visited:
                    visited[neighbour] = visited[cell] + 1
                    if neighbour == end:
                        part = "Part A: " if PART_A else "Part B: "
                        print(part, visited[neighbour])
                        not_found = False
                        break
                    next_level.append(neighbour)
        queue.append(next_level)




