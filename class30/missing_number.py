def solve(A):
    n = len(A)

    for i in range(n):
        while 0 < A[i] <= n and A[i] != i+1:
            if A[i] == A[A[i] -1]:
                break
            temp = A[A[i]-1]
            A[A[i]-1] = A[i]
            A[i] = temp

    for i in range(n):
        if A[i] != i +1:
            return i+1

    return n+1



A = [1, 2, 0]
A = [3, 4, -1, 1]
A = [-8, -7, -6]
print(solve(A))