def solve(A):

    n = len(A)
    m = len(A[0])
    max_sum = -(1 << 31)
    for i in range(n-1,-1,-1):
        for j in range(m-2,-1,-1):
            A[i][j] += A[i][j+1]

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i != n-1:
                A[i][j] += A[i+1][j]
            max_sum = max(max_sum,A[i][j])

    return max_sum


A =   [ [-5 ,-4, -3],
        [-1,  2,  3],
        [2 , 2,  4]
    ]
print(solve(A))