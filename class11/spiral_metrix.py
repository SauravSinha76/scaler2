def solve(A):
    mat = [[0] * A for _ in range(A)]
    n = 1
    i = 0
    j = 0
    while A > 1:
        for _ in range(1,A):
            mat[i][j] = n
            j += 1
            n += 1
        for _ in range(1,A):
            mat[i][j] = n
            i += 1
            n += 1
        for _ in range(1,A):
            mat[i][j] = n
            j -= 1
            n += 1
        for _ in range(1,A):
            mat[i][j] = n
            i -= 1
            n += 1
        i += 1
        j += 1
        A -= 2

    if A == 1:
        mat[i][j] = n
    return mat

print(solve(7))