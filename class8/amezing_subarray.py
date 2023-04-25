def solve(A):
    n = len(A)
    A = A.upper()
    vowal = "AEIOU"
    count =0
    ans =0
    for i in range(n-1,-1,-1):
        count += 1
        if A[i] in vowal:
            ans += count
    return ans

A ="ABEC"
print(solve(A))