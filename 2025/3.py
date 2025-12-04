testing = False
puzzle_number = 3
input_path = f"2025/{puzzle_number}.test" if testing else f"2025/{puzzle_number}.in"

with open(input_path, "r") as input:
    puzzle_input = input.read()

def joltage(bank: str, size: int) -> str:
    if len(bank) == size:
        return bank
    
    batteries = [int(battery) for battery in bank]
    if size == 1:
        return str(max(batteries))
    
    highest_left = max(batteries[:-size+1])
    
    left_index = batteries.index(highest_left)
    return bank[left_index] + joltage(bank[left_index+1:], size-1)


def part1(input):
    solution = 0
    banks = input.splitlines()
    for bank in banks:
        solution += int(joltage(bank, 2))
    return solution

def part2(input):
    solution = 0
    banks = input.splitlines()
    for bank in banks:
        if testing:
            print(joltage(bank, 12))
        solution += int(joltage(bank, 12))
    return solution

if __name__ == "__main__":
    print("Part 1:", part1(puzzle_input))
    print("Part 2:", part2(puzzle_input))
