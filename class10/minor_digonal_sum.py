def solve(A):
    n = len(A)
    digonal_sum =0
    i =0
    j = n-1
    while i < n and j > -1:
        digonal_sum += A[i][j]
        i += 1
        j -= 1

    return digonal_sum

A =[
    [1,-2,-3],
    [-4,5,-6],
    [-7,-8,9]
]
print(solve(A))