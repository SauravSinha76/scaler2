def solve(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans += ((i +1) * (n-i) * A[i])
    return ans

A = [1,2,3,4,5]
print(solve(A))