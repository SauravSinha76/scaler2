def solve(A):
    ans = 0
    for a in A:
        ans ^= a
    return ans

A = [1, 2, 2, 3, 1]
print(solve(A))