def merge(A,l,m,r):
    i = l
    j = m+1
    C = []
    inv_count =0

    while i <= m and j <= r:
        if A[i] <= A[j]:
            C.append(A[i])
            i += 1
        else:
            inv_count += (m - i +1)
            C.append(A[j])
            j += 1
    while i <= m:
        C.append(A[i])
        i += 1
    while j <= r:
        C.append(A[j])
        j += 1

    k = 0
    for i in range(l,r+1):
        A[i] = C[k]
        k += 1

    return inv_count

def merge_sort(A,l,r):
    if l == r:
        return 0

    mid = (l + r) // 2
    inv_count = 0
    inv_count += merge_sort(A,l,mid)
    inv_count += merge_sort(A,mid + 1, r)
    inv_count += merge(A,l,mid,r)

    return inv_count

def solve(A):
    l =0
    r = len(A) -1
    return merge_sort(A,l,r)

A = [1, 3, 2]
A = [3, 4, 1, 2]
print(solve(A))
