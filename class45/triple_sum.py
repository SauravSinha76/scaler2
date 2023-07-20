def solve(A,B):
    n = len(A)
    A.sort()
    min_diff = (1 << 31) - 1
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            p = A[i] + A[l] + A[r]
            diff = abs(B - p)
            if diff < min_diff:
                min_diff = diff
                ans = p
            if p < B:
                l += 1
            else:
                r -= 1
    return ans






A = [-1, 2, 1, -4]
B = 1
print(solve(A,B))