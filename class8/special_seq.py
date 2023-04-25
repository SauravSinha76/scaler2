def solve(A):
    n = len(A)
    ans =0
    c =0
    for i in range(n-1,-1,-1):
        if A[i] == 'G':
            c += 1
        elif A[i] == 'A':
            ans += c
    return ans

A = "ABCGAG"
print(solve(A))