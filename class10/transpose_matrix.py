def solve(A):
    row = len(A)
    column = len(A[0])

    ans =[]

    for i in range(row):
        r =[]
        for j in range(column):
            r.append(A[j][i])
        ans.append(r)

