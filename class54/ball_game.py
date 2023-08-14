from class54.Stack import Stack


def solve(A,B,C):
    stack = Stack()
    stack.push(B)
    for a in C:
        if a == 0 and stack.size != -1:
            stack.pop()
        else:
            stack.push(a)
    return stack.top()


A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]
A = 1
B = 1
C = [2]
print(solve(A,B,C))