def solve(A,B):
    hm_A = {}
    hm_B = {}

    stack=[]
    global_sign = True
    for a in A:
        if a =='(' and len(stack) != 0 and stack[-1] == '-':
            global_sign = not global_sign
            stack.append(a)
        elif a == ')':
            while len(stack) != 0 and stack[-1] != '(':
                stack.pop()
            stack.pop()
            if len(stack) != 0 and stack[-1] == '-':
                global_sign = not global_sign
        elif a.isalpha():
            if len(stack) != 0 and stack[-1] =='-':
                hm_A[a] = not global_sign
                stack.pop()
            else:
                hm_A[a] = global_sign
        else:
            stack.append(a)
    global_sign = True
    stack=[]
    for b in B:
        if b =='(' and len(stack) != 0 and stack[-1] == '-':
            global_sign = not global_sign
            stack.append(b)
        elif b == ')':
            while len(stack) != 0 and stack[-1] != '(':
                stack.pop()
            stack.pop()
            if len(stack) != 0 and stack[-1] == '-':
                global_sign = not global_sign
        elif b.isalpha():
            if len(stack) != 0 and stack[-1] == '-':
                hm_B[b] = not global_sign
                stack.pop()
            else:
                hm_B[b] = global_sign
        else:
            stack.append(b)
    if hm_A == hm_B:
        return 1
    else:
        return 0

A = "-(a+b+c)"
B = "-a-b-c"
print(solve(A,B))
