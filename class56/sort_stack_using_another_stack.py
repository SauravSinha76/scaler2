def solve(A):
    stack= []
    while A:
        temp = A[-1]
        A.pop()
        while stack and stack[-1] <= temp:
            x = stack[-1]
            stack.pop()
            A.append(x)
        stack.append(temp)

    while stack:
        A.append(stack[-1])
        stack.pop()

    return A

A = [5, 4, 3, 2, 1]
print(solve(A))
