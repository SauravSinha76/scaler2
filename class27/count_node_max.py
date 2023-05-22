from class27.TreeNode import TreeNode


def solve(A,max_val):
    if A == None:
        return 0
    if max_val < A.val:
        max_val = A.val
        return solve(A.left,max_val) + solve(A.right,max_val) + 1
    return solve(A.left,max_val) + solve(A.right,max_val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(3)
print(solve(root,0))