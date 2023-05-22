from class27.TreeNode import TreeNode


def solve(A):
    if A == None:
        return
    solve(A.left)
    print(A.val)
    solve(A.right)

def inorderTraversal(A):
    s = []
    current = A
    ans =[]
    while True:
        if current:
            s.append(current)
            current = current.left
        elif len(s) != 0:
            current = s.pop()
            ans.append(current.val)
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
print("-------------")
print(inorderTraversal(root))