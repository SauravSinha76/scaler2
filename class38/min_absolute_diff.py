def solve(A):
    n = len(A)
    A.sort()
    min_diff = 1 << 31 -1
    for i in range(n-1):
        min_diff = min(min_diff, A[i+1] - A[i])
    return min_diff

A = [3, 11, -1, 5]
print(solve(A))
