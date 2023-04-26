def solve(A,B,C):
    sum = 0
    for i in range(B):
        sum += A[i]

    s = 0
    e = B
    while e < len(A):
        if sum == C:
            return 1
        sum += (A[e] - A[s])
        s += 1
        e += 1
    return 0

A = [4, 3, 2, 6, 1]
B = 3
C = 11
A = [4, 2, 2, 5, 1]
B = 4
C = 6
print(solve(A,B,C))