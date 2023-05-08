def solve(A):
    n = len(A)

    max_val = max(A) + 1

    count=[0]*max_val

    for i in range(n):
        count[A[i]] += 1


    k = 0

    for i in range(max_val):
        for j in range(count[i]):
            A[k] = i
            k += 1
    return A

A = [4, 2, 1, 3]
A = [1, 3, 1]
print(solve(A))