def solve(A):
    n = len(A)
    ans =0
    for i in range(n):
        for j in range(n):
          ans += (A[i][j] * ((i+1)*(j+1) * (n-i)*(n-j)))
    return ans

A = [ [1, 2],
      [3, 4] ]
print(solve(A))