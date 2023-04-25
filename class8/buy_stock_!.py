import sys


def solve(A):
    n = len(A)

    max_profit =0
    min_val = sys.maxsize

    for i in range(n):
        if A[i] < min_val:
            min_val = A[i]
        max_profit = max(max_profit,A[i] - min_val)

    return max_profit

A = [7, 4, 5, 2, 4]
print(solve(A))