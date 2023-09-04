from collections import deque

from class58.Tree import TreeNode


def solve(A):
    queue = deque()
    n = len(A)
    root = TreeNode(A[0])
    queue.append(root)
    i = 1
    while i < n:
        curr = queue.popleft()
        if A[i] != -1:
            curr.left = TreeNode(A[i])
            queue.append(curr.left)
        i += 1
        if A[i] != -1:
            curr.right = TreeNode(A[i])
            queue.append(curr.right)
        i += 1

    return root





A=[1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]