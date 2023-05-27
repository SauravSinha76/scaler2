def solve(A,B):
    n = len(A)
    m =len(A[0])
    min_val = (1 << 31) -1
    i = 0
    j = m-1

    while i < n and j > -1:
        if A[i][j] >= B:
            if A[i][j] == B:
                min_val = min(min_val, (i+1) * 1009 + (j+1))
            j -= 1
        else:
            i += 1

    if min_val == 1 << 31:
        return -1
    return min_val

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2

A = [[1, 2],
     [3, 3]]
B = 3
print(solve(A,B))