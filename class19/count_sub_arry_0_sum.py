def solve(A):
    n = len(A)

    hs = {0:1}
    for i in range(1,n):
        A[i] += A[i-1]

    count = 0
    for a in A:
        if a in hs:
            count += hs[a]
        hs[a] = hs.get(a,0) +1
    return count

A = [1, -1, -2, 2]
A = [-1, 2, -1]
print(solve(A))