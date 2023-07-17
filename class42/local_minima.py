def solve(A):
    n = len(A)
    if A[0] < A[1]:
        return A[0]
    if A[n-1] < A[n-2]:
        return A[n-1]

    l = 1
    r = n-2

    while l <= r:
        mid = (l + r) // 2

        if A[mid-1] >A[mid] < A[mid +1]:
            return A[mid]
        elif A[mid +1] < A[mid]:
            l = mid +1
        else:
            r = mid -1

    return -1


A =[9,8,7,8,6,4,1,5]
print(solve(A))