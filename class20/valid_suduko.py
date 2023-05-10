def solve(A):
    for i in range(9):
        row = set()
        for j in range(9):
            if A[i][j] in row:
                return 0
            elif A[i][j] != '.':
                row.add(A[i][j])

        col = set()
        for j in range(9):
            if A[j][i] in col:
                return 0
            elif A[j][i] != '.':
                col.add(A[j][i])
        box = set()
        for j in range(9):
            m = j // 3 + 3 *(i // 3)
            n = j % 3 + 3 * (i % 3)
            if A[m][n] in box:
                return 0
            elif A[m][n] != '.':
                box.add(A[m][n])
    return 1

A= ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
     "....8..79"]
print(solve(A))

