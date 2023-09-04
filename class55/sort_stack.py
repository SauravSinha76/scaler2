def solve(A):
    stack =[]
    while A:
        temp = A[-1]
        A.pop()
        while stack and temp > stack[-1]:
            x = stack[-1]
            stack.pop()
            A.append(x)
        stack.append(temp)
    while stack:
        temp = stack[-1]
        stack.pop()
        A.append(temp)
    return A




A =[4,0,6,-1,5,12,8,11,9,7]
print(solve(A))