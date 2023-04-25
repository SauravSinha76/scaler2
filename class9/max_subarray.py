import sys


def solve(A,B,C):
    max_sum =- sys.maxsize
    for i in range(A):
        sum =0
        for j in range(i,A):
            sum += C[j]
            if B >= sum > max_sum:
                max_sum = sum
    return max_sum
A = 5
B = 12
C = [2, 1, 3, 4, 5]
print(solve(A,B,C))
