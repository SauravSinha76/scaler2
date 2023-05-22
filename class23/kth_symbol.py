def solve(A,B):
    if B == 0:
        return B
    val = solve(A-1, B// 2)
    if B % 2 == 0:
        return val
    else:
        return 1 - val


A = 3
B = 0
A = 4
B = 4
print(solve(A,B))