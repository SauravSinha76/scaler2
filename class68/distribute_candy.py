def solve(A):
    n = len(A)

    ans =[1] *n

    for i in range(1,n):
        if A[i] > A[i-1]:
            ans[i] = ans[i-1] +1

    for i in range(n-2,-1,-1):
        if A[i] > A[i+1] and ans[i] <= ans[i+1]:
            ans[i] = ans[i+1] + 1

    return sum(ans)


A = [1, 5, 2, 1]
print(solve(A))