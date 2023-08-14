from class54.Stack import Stack


def solve(A):
    stack = Stack()
    hm={'}':'{',
        ')':'(',
        ']':'['
        }
    for a in A:
        if stack.size != -1 and stack.top() == hm.get(a,''):
            stack.pop()
        else:
            stack.push(a)

    if stack.size != -1:
        return 0
    else:
        return 1



A = '{([])'
print(solve(A))