def solve(A):
    n = len(A)
    max_ele = A[0]
    second_max_ele = -1
    for i in range(1,n):
        if max_ele < A[i]:
            second_max_ele = max_ele
            max_ele = A[i]
        elif A[i] > second_max_ele and A[i] != max_ele:
            second_max_ele = A[i]

    return second_max_ele
