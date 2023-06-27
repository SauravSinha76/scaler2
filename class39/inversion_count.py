def solve_brt(A):
    n = len(A)
    count =0
    for i in range(n):
        for j in range(i,n):
            if A[i] > A[j]:
                count += 1
    return count

def merge(A,l,m,r):
    i = l
    j = m + 1
    inv_count = 0
    C =[]
    while i <=m and j <= r:
        if A[i] < A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            inv_count += (m - i +1)
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

def invers_count(A,l,r):
    if l == r:
        return 0
    inv_count = 0
    mid = (l+r) // 2
    
    inv_count += invers_count(A,l,mid)
    inv_count += invers_count(A,mid+1,r)
    inv_count += merge(A,l,mid,r)
    return inv_count

def solve(A):
    return invers_count(A,0,len(A)-1)
A = [10,3,8,15,6,12,2,18,7,1]
print(solve_brt(A))
print(solve(A))