def solve(A):
    count = 0
    i = 0

    for i in range(len(A)):
        while A[i] != i:
                tmp = A[A[i]]
                A[A[i]] = A[i]
                A[i] = tmp
                count += 1

    return count

A = [1, 2, 3, 4, 0]
print(solve(A))