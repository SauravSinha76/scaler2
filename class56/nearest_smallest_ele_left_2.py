def solve(A):
    n = len(A)
    stack =[]
    ans = []
    for i in range(n):
        while stack and stack[-1] >= A[i]:
            stack.pop()

        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(A[i])
    return ans


A = [4, 5, 2, 10, 8]
print(solve(A))