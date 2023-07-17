def solve(A,B):
    n = len(A)

    l = 0
    r = n-1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == B:
            return mid
        if A[mid] < B:
            l = mid +1
        else:
            r = mid -1

    return l
A = [1, 3, 5, 6]
B = 5

A = [1, 4, 9]
B = 3
print(solve(A,B))