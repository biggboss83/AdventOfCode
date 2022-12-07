input_path = "2022/7.in"

ROOT = '/'
TOTAL = 70000000
NEEDED = 30000000
fs = dict()
dirs = set()

def cd(dir, arg):
    if arg == ROOT:
        return ROOT
    elif arg == "..":
        dir_lst = dir.split(ROOT)
        if len(dir_lst) <= 3:
            return ROOT
        else:
            return ROOT.join(dir_lst[:-2]) + ROOT
    else:
        return dir + arg + ROOT

def get_size(path):
    size = 0
    for key in fs.keys():
        if key.startswith(path):
            size += fs[key]
    return size


with open(input_path, "r") as input:
    pwd = ROOT
    lines = [line.strip().split() for line in input.readlines()]
    for line in lines:
        if line[0] == '$':
            if line[1] == "cd":
                pwd = cd(pwd, line[2])
            elif line[1] == "ls":
                dirs.add(pwd)
        elif line[0] == "dir":
            dir = cd(pwd, line[1])
            fs[dir] = 0
        else:
            fs[pwd+line[1]] = int(line[0])

parta = sum([get_size(dir) for dir in dirs if get_size(dir) <= 100000])
print("Part A: ", parta)

FREE = TOTAL - get_size(ROOT)

partb = sorted([get_size(dir) for dir in dirs if get_size(dir) >= NEEDED - FREE])
print("Part B: ", partb[0])