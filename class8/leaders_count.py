def solve(A):
    n = len(A)
    leader = [A[n-1]]
    max_ele = A[n-1]

    for i in range(n-2,-1,-1):
        if max_ele < A[i]:
            max_ele = A[i]
            leader.append(A[i])
    return leader

A = [16, 17, 4, 3, 5, 2]
print(solve(A))