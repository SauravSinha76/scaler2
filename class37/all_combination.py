def comb(arr, n, B, x, ans):
    if n == B:
        print(x)
        ans.append("".join(x))
        return

    x.append(arr[n])
    comb(arr, n + 1, B, x, ans)
    x.pop()
    comb(arr, n + 1, B, x, ans)


def solve(A):
    arr = A
    n = 0
    B = len(A)
    x = []
    ans = []
    comb(arr, n, B, x, ans)
    return ans


def makeCombiUtil(n, left, k, tmp, ans):
    # Pushing this vector to a vector of vector
    if k == 0:
        ans.append(list(tmp))
        return

    # i iterates from left to n. First time
    # left will be 1
    for i in range(left, n + 1):
        tmp.append(i)
        makeCombiUtil(n, i + 1, k - 1, tmp, ans)

        # Popping out last inserted element
        # from the vector
        tmp.pop()

def solve_comb(A,B):
    tmp =[]
    ans =[]
    makeCombiUtil(A,1,B,tmp,ans)
    return ans

print(solve("saurav"))
print(solve_comb(6,3))