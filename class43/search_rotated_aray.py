def find_pivote(A, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = low + (high - low) // 2

    if mid < high and A[mid] > A[mid + 1]:
        return mid
    if mid > low and A[mid] < A[mid - 1]:
        return mid - 1
    if A[low] >= A[mid]:
        return find_pivote(A, low, mid - 1)
    return find_pivote(A, mid + 1, high)
def binery_search(A,left,right,key):
    while left <= right:
        mid = (left + right) // 2

        if A[mid] == key:
            return mid
        if A[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def pivot(A):
    l = 0
    r = len(A)-1

    while l <= r:
        mid = (l+ r) // 2

        if mid < r and A[mid] > A[mid +1]:
            return mid
        if l < mid and A[mid] < A[mid -1]:
            return mid -1
        if A[mid] < A[l]:
            r = mid -1
        else:
            l = mid + 1
    return -1

def solve(A,B):
    left = 0
    right = len(A) -1
    p = pivot(A)

    if p == -1:
        return binery_search(A,left,right,B)
    if A[p] == B:
        return p
    if A[0] <= B:
        return binery_search(A,left,p , B)
    return binery_search(A,p+1,right,B)

A =[3,4,5,6,7,8,9,0,1,2]
print(find_pivote(A,0,len(A)-1))
print(pivot(A))
print(solve(A,3))