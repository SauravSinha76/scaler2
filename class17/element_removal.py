def solve(A):
    A.sort(reverse= True)
    cost = 0
    n = len(A)
    for i in range(n):
        cost += (A[i] * (i+1))

    return cost

A = [2, 1]
print(solve(A))