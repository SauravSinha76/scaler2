import sys


def solve(A,B):
    n = len(A)
    sum =0
    i = 0
    while i < B:
        sum += A[i]
        i += 1
    j = n-1
    max_sum = - sys.maxsize
    while i > 0:
        sum += (A[j] -A[i-1])
        j -=1
        i -=1
        max_sum = max(max_sum,sum)

    return max_sum

A = [2, 3, -1, 4, 2, 1]
B = 4
print(solve(A,B))

