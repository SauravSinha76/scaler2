def solve(A):
    n = len(A)
    ans = 0
    for i in range(1,n-1):
        l =0
        r = 0
        for j in range(i-1,-1,-1):
            if A[i] > A[j]:
                l += 1
        for j in range(i+1,n):
            if A[i] < A[j]:
                r += 1
        ans += (l*r)
    return ans

A = [1, 2, 4, 3]
print(solve(A))