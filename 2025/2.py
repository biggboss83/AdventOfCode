testing = False
input_path = "2025/2.test" if testing else "2025/2.in"

with open(input_path, "r") as input:
    puzzle_input = input.read()

part1 = 0
part2 = 0

# Part 1
def invalid_id(id: int) -> int:
    id_str = str(id)
    id_len = len(id_str)
    if id_len % 2:
        return 0
    first_half = id_str[:id_len//2]
    second_half = id_str[id_len//2:]
    if first_half == second_half:
        return int(id_str)
    return 0
    
IDranges = puzzle_input.split(",")
for IDrange in IDranges:
    first, last = IDrange.split("-")
    for id in range(int(first), int(last)+1):
        part1 += invalid_id(id)

print("Part 1: ", part1)

#Part 2
def subdivisors(num: int):
    return (i for i in range(1, num) if num % i == 0)

def split_string(string: str, size: int) -> list[str]:
    assert(size <= len(string))
    return [string[i:i+size] for i in range(0, len(string), size)]

def repeated_parts(id_parts: list[int]) -> int:
    return all(id_part == id_parts[0] for id_part in id_parts)

def invalid_id(id: int) -> int:
    id_str = str(id)
    for div in subdivisors(len(id_str)):
        id_parts = list(map(int, split_string(id_str, div)))
        if testing:
            print(id, id_parts)
        if repeated_parts(id_parts):
            return id
    return 0

def ids_list(IDrange: str) -> list[int]:
    first, last = map(int, IDrange.split("-"))
    return list(range(first, last+1))

for IDrange in IDranges:
    for id in ids_list(IDrange):
        part2 += invalid_id(id)


print("Part 2: ", part2)
    