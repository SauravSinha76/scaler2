def merge(A,l,m,r):
    i = l
    j = m+1
    C =[]
    while i <= m and j <= r:
        if A[i] <= A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1

    while i <= m:
        C.append(A[i])
        i += 1

    while j <= r:
        C.append(A[j])
        j += 1

    for k in range(len(C)):
        A[k+l] = C[k]

def merge_sort(A,l,r):
    if l == r:
        return
    mid = (l + r) // 2

    merge_sort(A,l,mid)
    merge_sort(A, mid+1 ,r)
    merge(A,l,mid,r)

def sort(A):
    l = 0
    r = len(A)-1
    merge_sort(A,l,r)
    return A

A =[9,3,3,-4,5,1,6,7,-2,11,4,5]
print(sort(A))

