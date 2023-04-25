def solve(A):
    vowels = "AEIOU"
    A =A.upper()
    n = len(A)
    ans =0
    c = 0
    for i in range(n-1,-1,-1):
        c += 1
        if A[i] in vowels:
            ans += c
    return ans % 1003


A = "ABEC"
print(solve(A))