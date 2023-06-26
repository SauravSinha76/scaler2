def solve(A):
    n = len(A)

    A.sort()
    max_magic = 0
    min_magic = 0
    j =0
    i = 0
    while i < n//2:
        max_magic += A[n-1-i] - A[i]
        i += 1

        min_magic += A[j+1] - A[j]
        j += 2

    return [max_magic,min_magic]

A = [3, 11, -1, 5]
print(solve(A))