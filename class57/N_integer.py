from collections import deque


def solve(A):
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    ans =[]
    for i in range(3,A,3):
        x = queue.popleft()
        ans.append(x)
        queue.append(10 *x +1)
        queue.append(10* x+ 2)
        queue.append(10* x+3)
    for a in queue:
        ans.append(a)

    return ans
print(solve(10))

