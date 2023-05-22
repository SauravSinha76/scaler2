def solve(A):
    if A == 0:
        return 0

    r = A % 10
    A = A // 10
    return solve(A) + r


print(solve(123))