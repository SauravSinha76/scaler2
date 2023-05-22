from class27.TreeNode import TreeNode


def solve(A):
    if A == None:
        return
    solve(A.left)
    solve(A.right)
    print(A.val)

def postorderTraversal(A):
    s = []
    current = A
    ans =[]
    while True:
        if current:
            s.append(current)
            s.append(current)
            current = current.left
        elif len(s) != 0:
            current = s.pop()
            if len(s) > 0 and current == s[-1]:
                current = current.right
            else:
                ans.append(current.val)
                current = None
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
print(postorderTraversal(root1))