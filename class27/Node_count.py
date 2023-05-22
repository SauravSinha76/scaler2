from class27.TreeNode import TreeNode


def count(A):
    if A == None:
        return 0
    return count(A.left) + count(A.right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(count(root))