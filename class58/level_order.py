from collections import deque

from class58.Tree import Tree


def solve(A):
    queue = deque()
    queue.append(A)
    dummy = Tree(-1)
    queue.append(dummy)
    ans =[]
    row =[]
    while len(queue) > 1:
        curr = queue.popleft()
        if curr == dummy:
            queue.append(curr)
            ans.append(row)
            row = []
        else:
            row.append(curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
    ans.append(row)
    return ans

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
print(solve(root))
