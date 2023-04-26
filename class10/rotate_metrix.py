def solve(A):
    n = len(A)

    for i in range(n):
        for j in range(i+1,n):
            A[i][j],A[j][i] = A[j][i],A[i][j]
    for i in range(n):
        l = 0
        r = n-1
        while l < r:
            A[i][l], A[i][r] = A[i][r],A[i][l]
            l += 1
            r -= 1
    print(A)



A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]
print(solve(A))