def solve(A):
    i = 1
    while i * i <= A:
        if i * i == A:
            return i
        i += 1
    return -1

print(solve(8))