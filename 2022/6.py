input_path = "2022/6.in"

with open(input_path, "r") as input:
    temp = list(input.read().strip())
    A = 4
    B = 14
    for i in range(A, len(temp)):
        lst = list(temp[i-A:i])
        if len(lst) == len(set(lst)):
            print("Part A: ", i)
            break
    for j in range(B, len(temp)):
        lst = list(temp[j-B:j])
        if len(lst) == len(set(lst)):
            print("Part B: ", j)
            break

