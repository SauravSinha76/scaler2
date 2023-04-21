def solve(A):
    n = len(A)
    min_ele = A[0]
    max_ele = A[0]

    for i in range(1,n):
        if min_ele > A[i]:
            min_ele = A[i]
        if max_ele < A[i]:
            max_ele = A[i]
    return max_ele + min_ele

A = [-2, 1, -4, 5, 3]
print(solve(A))