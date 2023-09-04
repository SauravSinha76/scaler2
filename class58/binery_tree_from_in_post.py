from class58.Tree import TreeNode


def inorder(root):
    while root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def build_tree(in_ord,post,start,end,pos):
    if start > end:
        return
    root = TreeNode(post[pos])
    idx = in_ord[post[pos]]
    root.right = build_tree(in_ord,post,idx+1,end,pos-1)
    root.left = build_tree(in_ord,post,start,idx -1, pos - (end - idx) -1)
    return root

def solve(A,B):
    in_ord ={}
    n = len(A)
    for i in range(n):
        in_ord[A[i]] = i

    return build_tree(in_ord,B,0,n-1,n-1)




A = [6, 1, 3, 2]
B = [6, 3, 2, 1]
inorder(solve(A,B))
