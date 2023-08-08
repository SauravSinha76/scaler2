def solve(A):
    n = len(A)

    hm ={}
    ans = 1 << 31
    for i in range(n):
        if A[i] not in hm:
            hm[A[i]] = i
        else:
            dist = i - hm[A[i]]
            ans = min(dist, ans)
            hm[A[i]] = i

    if ans == 1 << 31:
        return -1
    return ans

A = [7, 1, 3, 4, 1, 7]
A = [1, 1]
print(solve(A))