def solve(A):
    n = len(A)
    ans =[]

    for i in range(n):
        r = [0 for _ in range(n)]
        row = 0
        column = i
        k = 0
        while row < n and column > -1:
            r[k] = A[row][column]
            k += 1
            row += 1
            column -= 1
        ans.append(r)
    for i in range(1,n):
        r = [0 for _ in range(n)]
        row = i
        column = n-1
        k = 0
        while row < n and column > -1:
            r[k] = A[row][column]
            k += 1
            row += 1
            column -= 1
        ans.append(r)
    return ans

A=[
    [1,-2,-3],
    [-4,5,-6],
    [-7,-8,9]
]
print(solve(A))