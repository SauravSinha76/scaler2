def solve(A):
    n = len(A)
    diagonal_sum =0
    i =0
    j =0
    while i <n and j < n:
        diagonal_sum += A[i][j]
        i += 1
        j += 1

    return diagonal_sum

A =[
    [1,-2,-3],
    [-4,5,-6],
    [-7,-8,9]
]
print(solve(A))
