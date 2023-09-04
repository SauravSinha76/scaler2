def solve(A):
    stack=[]
    ans =[]
    for a in A:
        while stack and stack[-1] >= a:
            stack.pop()

        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])

        stack.append(a)
    return ans



A = [4,5,2,10,8,2]
print(solve(A))