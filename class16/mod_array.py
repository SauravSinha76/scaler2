def solve(A,B):
    t = 1
    ans = 0
    n = len(A)
    for i in range(n-1,-1,-1):
        ans = (A[i] * t + ans) % B
        t = (t * 10) % B

    return ans

A = [1, 4, 3]
B = 2
print(solve(A,B))
