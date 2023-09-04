from class58.Tree import Tree


def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def itrative(root):
    curr = root
    stack =[]
    ans =[]

    while curr or stack:
        while curr:
            stack.append(curr)
            ans.append(curr.val)
            curr = curr.left

        node = stack.pop()
        curr = node.right

    return ans

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
preorder(root)
print(itrative(root))