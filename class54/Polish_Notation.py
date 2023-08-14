from class54.Stack import Stack

def evaluate(first,op,second):
    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    else:
        return first // second

def solve(A):
    stack = Stack()
    ops=['+','-','*','/']
    for a in A:
        if a in ops:
            second = stack.pop()
            first = stack.pop()
            val = evaluate(first,a,second)
            stack.push(val)
        else:
            stack.push(int(a))
    return stack.pop()

A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
print(solve(A))