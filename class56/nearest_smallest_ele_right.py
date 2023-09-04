def solve(A):
    stack=[]
    ans =[]
    for i in range(len(A)-1,-1,-1):
        while stack and stack[-1] >= A[i]:
            stack.pop()

        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])

        stack.append(A[i])
    ans.reverse()
    return ans



A = [4,5,2,10,8,2]
print(solve(A))