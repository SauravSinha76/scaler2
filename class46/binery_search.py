def binery_search(A,B):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            return mid
        if A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1

def floor(A,B):
    n = len(A)
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1
    return r

def celining(A,B):
    n = len(A)
    l = 0
    r = n - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1
    return l


A =[1,4, 7, 9, 12, 15 , 19, 24]
print(binery_search(A,7))
print(floor(A,6))
print(celining(A,8))