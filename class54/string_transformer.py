from class54.Stack import Stack


def solve(A):
    stack = Stack()

    for a in A:
        if stack.size != -1 and stack.top() == a:
            stack.pop()
        else:
            stack.push(a)

    ans = ''
    while stack.size > -1:
        ans += stack.pop()

    return ans[::-1]

A = "abccbc"
print(solve(A))