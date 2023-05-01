import sys


def solve(A,B):
    n = len(A)
    min_cost = sys.maxsize
    for i in range(1,n-1):
        left = sys.maxsize
        right = sys.maxsize
        for j in range(i-1,-1,-1):
            if A[j] < A[i]:
                left = min(left, B[j])
        for j in range(i+1,n):
            if A[j] > A[i]:
                right = min(right,B[j])
        min_cost = min(min_cost, left + B[i]+right)
    if min_cost == sys.maxsize:
        return -1
    else:
        return min_cost

A = [1, 3, 5]
B = [1, 2, 3]
# A = [1, 6, 4, 2, 6, 9]
# B = [2, 5, 7, 3, 2, 7]
print(solve(A,B))