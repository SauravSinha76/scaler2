from class27.TreeNode import TreeNode


def sum(A):
    if A == None:
        return 0
    return sum(A.left) + sum(A.right) + A.val

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(sum(root))