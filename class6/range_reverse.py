def solve(A,B,C):

    while B < C:
        A[B],A[C] = A[C],A[B]
        B += 1
        C -= 1

    return A

A = [1, 2, 3, 4]
B = 2
C = 3
print(solve(A,B,C))