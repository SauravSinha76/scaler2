def solve(A):
    row = len(A)
    column= len(A[0])
    ans=[]
    for i in range(row):
        row_sum = 0
        for j in range(column):
            row_sum += A[i][j]
        ans.append(row_sum)

    return ans

A = [
[1,2,3,4],
[5,6,7,8],
[9,2,3,4],
]
print(solve(A))