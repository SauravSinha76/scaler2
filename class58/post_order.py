from class58.Tree import Tree


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)

def itrative(root):
    curr = root
    stack =[]
    ans =[]

    while curr or stack:
        while curr:
            stack.append(curr)
            stack.append(curr)
            curr = curr.left

        node = stack.pop()
        if stack and node.val == stack[-1].val:
            curr = node.right
        else:
            ans.append(node.val)
            curr = None

    return ans

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
postorder(root)
print(itrative(root))