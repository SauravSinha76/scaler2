def solve(A,B):
    n = len(A)

    k = 0
    for i in range(n):
        if A[i] <= B:
            k += 1
    swap =0
    for i in range(k):
        if A[i] > B:
            swap += 1

    min_swap =swap
    s = 0
    e = k
    while e < n:
        if A[s] > B:
            swap -= 1
        if A[e] > B:
            swap += 1

        min_swap = min(min_swap,swap)
        s += 1
        e += 1
    return min_swap

A = [1, 12, 10, 3, 14, 10, 5]
B = 8

A = [5, 17, 100, 11]
B = 20
print(solve(A,B))