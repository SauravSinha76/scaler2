from class58.Tree import TreeNode


def inorder(root):
    while root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def itrative(root):
    curr = root
    stack =[]
    ans =[]
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        node = stack.pop()
        ans.append(node.val)
        curr = node.right
    return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
inorder(root)
print(itrative(root))
