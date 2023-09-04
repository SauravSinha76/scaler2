from collections import deque


def solve(A,B):

    queue = deque()

    max_ans =[]
    n = len(A)

    for i in range(B):

        while queue and A[i] > queue[-1]:
            queue.pop()
        else:
            queue.append(A[i])

    max_ans.append(queue[0])

    for i in range(1,n-B+1):
        leaving = A[i-1]
        if leaving == queue[0]:
            queue.popleft()
        while queue and A[i + B - 1] > queue[-1]:
            queue.pop()
        else:
            queue.append(A[i + B -1])
        max_ans.append(queue[0])
    print(max_ans)
    queue = deque()
    min_ans=[]
    for i in range(B):
        while queue and A[i] < queue[-1]:
            queue.pop()
        else:
            queue.append(A[i])

    min_ans.append(queue[0])

    for i in range(1, n - B +1):
        leaving = A[i-1]
        if leaving == queue[0]:
            queue.popleft()
        while queue and A[i + B -1] < queue[-1]:
            queue.pop()
        else:
            queue.append(A[i + B -1])
        min_ans.append(queue[0])
    print(min_ans)
    ans  =0
    for i in range(len(min_ans)):
        ans += min_ans[i] + max_ans[i]
    return ans

A = [2, 5, -1, 7, -3, -1, -2]
B = 4
print(solve(A,B))