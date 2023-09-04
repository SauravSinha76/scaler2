from collections import deque

from class58.Tree import TreeNode


def solve(A):
    queue = deque()
    queue.append(A)
    ans = []
    while queue:
        curr = queue.popleft()
        if curr is None:
            ans.append(-1)
        else:
            ans.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)

    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(solve(root))

