def solve(A):
    n = len(A)
    stack =[]
    ans =[-1] * n

    for i in range(n-1,-1,-1):
        while stack and stack[-1] <= A[i]:
            stack.pop()

        if not stack:
            ans[i] = -1
        else:
            ans[i] = stack[-1]

        stack.append(A[i])

    return ans

A = [4, 5, 2, 10]
print(solve(A))
