class Stack:
    def __init__(self):
        self.stack =[]


    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def get_middle(self):
        idx = len(self.stack)// 2
        return self.stack[idx]

    def delete_middle(self):
        idx = len(self.stack)// 2
        self.stack.remove(self.stack[idx])


def solve(A):
    stack = Stack()
    ans=[]
    for a in A:
        type = a[0]
        val =a[1]

        if type == 1:
            stack.push(val)
        elif type == 2:
            ans.append(stack.pop())
        elif type == 3:
            ans.append(stack.get_middle())
        else:
            stack.delete_middle()
    return ans


A = [
        [1, 3],
        [3, 0],
        [4, 0],
        [2 ,0],
        [1, 5],
        [1, 9],
        [3, 0]
     ]

A = [
        [1, 1],
        [1, 2],
        [1, 3],
        [3, 0],
        [4, 0],
        [3, 0],
        [4, 0]
     ]
print(solve(A))