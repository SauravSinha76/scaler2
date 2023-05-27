from class27.TreeNode import TreeNode


def solve(A,isLeft):
    if A is None:
        return 0
    if isLeft and A.left is None and A.right is None:
        return A.val
    return solve(A.left,True) + solve(A.right,False)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(3)
print(solve(root,False))