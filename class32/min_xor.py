def solve(A):

    n = len(A)

    A.sort()
    min_xor = 1 << 31 -1

    for i in range(1,n):
        min_xor = min(min_xor, A[i] ^ A[i-1])
    return min_xor


A = [0, 2, 5, 7]
A = [0, 4, 7, 9]
print(solve(A))