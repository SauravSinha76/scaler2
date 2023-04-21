def solve(A):
    n = len(A)

    for i in range(1,n):
        A[i] += A[i-1]

    for i in range(n):
        if i ==0 and A[n-1] == A[i]:
            return 0
        elif A[i-1] == A[n-1] - A[i]:
            return i



