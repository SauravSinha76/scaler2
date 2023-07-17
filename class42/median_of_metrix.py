def count_smaller(A,B):
    l = 0
    r = len(A) -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == B:
            return mid
        if A[mid] < B:
            l = mid +1
        else:
            r = mid -1
    return l


def solve(A):

    n = len(A)
    m = len(A[0])

    l = A[0][0]
    r = A[0][m-1]
    for i in range(1,n):
        l = min(l,A[i][0])
        r = max(r,A[i][m-1])


    k = (n * m) // 2
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        p = 0
        for i in range(n):
            p += count_smaller(A[i],mid)

        if p <= k:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ]
print(solve(A))