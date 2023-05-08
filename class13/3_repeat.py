import sys


def solve(A):
        n = len(A)
        first = sys.maxsize
        second = sys.maxsize
        count1= 0
        count2 = 0

        for i in range(n):
            if A[i] == first:
                count1 += 1
            elif A[i] == second:
                count2 += 1
            elif count1 == 0:
                first = A[i]
                count1 += 1
            elif count2 == 0:
                second = A[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0
        for i in range(n):
            if A[i] == first:
                count1 += 1
            elif A[i] == second:
                count2 += 1

        if count1 > n// 3:
            return first
        if count2 > n // 3:
            return  second

        return -1

A = [1, 2, 3, 1, 1]
A = [1, 2, 3]
print(solve(A))


