def solve(A):
    n = len(A)
    i = 0
    j = n-1
    count = 0
    row = -1
    while i < n and j > -1:
        if A[i][j] == 1:
            count += 1
            row = i
            j -= 1
        else:
            i += 1

    return row

A = [   [0, 1, 1],
         [0, 0, 1],
         [0, 1, 1]   ]

A = [   [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 1]    ]
print(solve(A))