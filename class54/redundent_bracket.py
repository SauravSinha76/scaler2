def solve(A):
    symbol =['+','-','*','/']
    stack = []
    for a in A:
        if  a == ')':
            flag = True
            while len(stack) != 0 and stack[-1] != '(':
                if stack[-1] in symbol:
                    flag = False
                stack.pop()
            stack.pop()

            if flag:
                return 1
        else:
            stack.append(a)
    return 0

A = "((a+b))"
A = "(a+(a+b))"
print(solve(A))