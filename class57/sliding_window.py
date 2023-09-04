from collections import deque


def solve(A,B):
    queue = deque()
    ans =[]
    for i in range(B):
        while queue and A[i] > queue[-1]:
            queue.pop()
        else:
            queue.append(A[i])

    ans.append(queue[0])
    n = len(A)
    for i in range(1, n - B + 1):
        leaving = A[i-1]
        if leaving == queue[0]:
            queue.popleft()

        while queue and A[i + B -1] > queue[-1]:
            queue.pop()
        else:
            queue.append(A[i + B -1])

        ans.append(queue[0])
    return ans

A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print(solve(A,B))
