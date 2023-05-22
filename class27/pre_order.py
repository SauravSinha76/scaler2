from class27.TreeNode import TreeNode


def solve(A):
    if A == None:
        return
    print(A.val)
    solve(A.left)
    solve(A.right)


def preorderTraversal(A):
    s = []
    current = A
    ans =[]
    while True:
        if current:
            s.append(current)
            ans.append(current.val)
            current = current.left
        elif len(s) != 0:
            current = s.pop()
            current = current.right
        else:
            break
    return ans
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root1 = root
solve(root1)
print(preorderTraversal(root1))