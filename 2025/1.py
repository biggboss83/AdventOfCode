testing = False
input_path = "2025/1.test" if testing else "2025/1.in"

with open(input_path, "r") as input:
    puzzle_input = input.read().splitlines()

dial = 50
dial_size = 100
count_zeroes = 0

def turn_right(current: int, clicks: int) -> int:
    return (current + clicks) % dial_size

def turn_left(current: int, clicks: int) -> int:
    return (current - clicks) % dial_size

def turn_dial(current: int, direction: str, clicks: int) -> int:
    if direction == "R":
        return turn_right(current, clicks)
    elif direction == "L":
        return turn_left(current, clicks)
    else:
        raise ValueError(f"Invalid direction: {direction}")
    
for line in puzzle_input:
    direction = line[0]
    clicks = int(line[1:])
    dial = turn_dial(dial, direction, clicks)
    if dial == 0:
        count_zeroes += 1

print("Part 1:")
print(count_zeroes)


print("Part 2:")
dial = 50
count_zeroes = 0
for line in puzzle_input:
    direction = line[0]
    circles, clicks = divmod(int(line[1:]), dial_size)
    count_zeroes += circles
    for _ in range(clicks):
        dial = turn_dial(dial, direction, 1)
        if dial == 0:
            count_zeroes += 1

print(count_zeroes)
    