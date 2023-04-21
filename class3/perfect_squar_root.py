def solve(A):
    i = 1
    while i * i <= A:
        if i * i == A:
            return 1
        i += 1
    return 0

print(solve(10000))