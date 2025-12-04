testing = False
puzzle_number = 4
input_path = f"2025/{puzzle_number}.test" if testing else f"2025/{puzzle_number}.in"

with open(input_path, "r") as input:
    puzzle_input = input.read()

def parse(input: str):
    return [list(line) for line in input.splitlines()]

def neighbours(x, y, max_x, max_y):
    adjacent = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # left, right, up, down, diagonals
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            adjacent.append((nx, ny))
    return adjacent

def adjacency_count(grid):
    max_x, max_y = len(grid[0]), len(grid)
    count = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for y in range(max_y):
        for x in range(max_x):
            for nx, ny in neighbours(x, y, max_x, max_y):
                if grid[ny][nx] == "@":
                    count[y][x] +=1
    return count
            

def part1(input):
    solution = 0
    adjacent = adjacency_count(input)
    max_x, max_y = len(input[0]), len(input)
    for y in range(max_y):
        for x in range(max_x):
            if input[y][x] == "@" and adjacent[y][x] < 4:
                solution += 1
    return solution

def part2(input):
    solution = 0
    keep_going = True
    while(keep_going):
        current_run = 0
        adjacent = adjacency_count(input)
        max_x, max_y = len(input[0]), len(input)
        for y in range(max_y):
            for x in range(max_x):
                if input[y][x] == "@" and adjacent[y][x] < 4:
                    input[y][x] = "."
                    current_run += 1
        if current_run == 0:
            keep_going = False
        else:
            solution += current_run
    return solution

if __name__ == "__main__":
    #print("Part 1:", part1(parse(puzzle_input)))
    print("Part 2:", part2(parse(puzzle_input)))
