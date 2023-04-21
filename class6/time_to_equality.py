def solve(A):
    return max(A) * len(A) - sum(A)

A = [2, 4, 1, 3, 2]
print(solve(A))