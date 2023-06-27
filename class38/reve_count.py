def solve(A):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if A[i] > 2*A[j]:
                count += 1
    return count

A = [1, 3, 2, 3, 1]
A = [4, 1, 2]
print(solve(A))
