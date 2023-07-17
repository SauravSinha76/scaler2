def count_smaller(A,key):
    l = 0
    r = len(A) -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == key:
            return mid
        if A[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return l

def solve(A,B):
    n = len(A)
    m = len(B)

    k = (m+n)//2

    l = min(A[0],B[0])
    r = max(A[-1],B[-1])
    x = get_median(A, B, k, l, r)
    if (m+n) % 2 == 0:
        k -= 1
        y = get_median(A,B,k,l,r)
        return (x+y)/2
    return float(x)



def get_median(A, B, k, l, r):
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        idx = count_smaller(A, mid)
        idx += count_smaller(B, mid)

        if idx <= k:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


A = [1, 4, 5]
B = [2, 3]

A = [1, 2, 3]
B = [4]
print(solve(A,B))