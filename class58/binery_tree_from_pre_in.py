from class58.Tree import TreeNode


def inorder(root):
    while root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def build_tree(in_ord,pre,start,end,pos):
    if start > end:
        return
    root = TreeNode(pre[pos])
    idx = in_ord[pre[pos]]
    root.right = build_tree(in_ord,pre,idx+1,end,pos+ idx +1)
    root.left = build_tree(in_ord,pre,start,idx -1, pos +1)
    return root

def solve(A,B):
    in_ord ={}
    n = len(A)
    for i in range(n):
        in_ord[B[i]] = i

    return build_tree(in_ord,A,0,n-1,0)

A = [1, 6, 2, 3]
B = [6, 1, 3, 2]

inorder(solve(A,B))