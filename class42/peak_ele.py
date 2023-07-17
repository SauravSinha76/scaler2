def solve(A):
    n = len(A)

    if A[0] > A[1]:
        return A[0]
    if A[n-1] > A[n-2]:
        return A[n-1]

    l = 1
    r = n-2

    while l <= r:
        mid = (l + r) // 2

        if A[mid-1] < A[mid] > A[mid + 1]:
            return A[mid]
        elif A[mid - 1] > A[mid]:
            r = mid -1
        else:
            l = mid + 1

    return -1

A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
print(solve(A))