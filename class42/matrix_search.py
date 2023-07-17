def solve(A,B):
    n = len(A)
    m = len(A[0])

    i = 0
    j = m-1

    while i < n and j > -1:
        if A[i][j] == B:
            return 1
        if A[i][j] > B:
            j -= 1
        else:
            i += 1
    return 0

A = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
B = 4

print(solve(A,B))