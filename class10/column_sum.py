def solve(A):
    row = len(A)
    column= len(A[0])
    ans=[]
    for j in range(column):
        column_sum = 0
        for i in range(row):
            column_sum += A[i][j]
        ans.append(column_sum)

    return ans

A = [
[1,2,3,4],
[5,6,7,8],
[9,2,3,4],
]
print(solve(A))