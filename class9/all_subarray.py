def solve(A):
    n = len(A)
    ans =[]
    for i in range(n):
        for j in range(i,n):
            ans.append(A[i:j+1])
    return ans

A = [1,2,3]
print(solve(A))