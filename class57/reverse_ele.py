def solve(A,B):
    stack =[]

    for i in range(B):
        stack.append(A[i])

    i = 0
    while stack:
        A[i] = stack[-1]
        stack.pop()
        i += 1

    return A

A = [1, 2, 3, 4, 5]
B = 3
A = [5, 17, 100, 11]
B = 2
print(solve(A,B))


