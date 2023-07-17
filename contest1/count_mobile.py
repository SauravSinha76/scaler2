def binery_search(A,B):
    l = 0
    r = len(A) -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == B:
            return mid
        if A[mid] < B:
            l = mid + 1
        else:
            r = mid -1
    return r

def solve(A,B):
    for i in range(1,len(A)):
        A[i] += A[i-1]

    res =[]
    for i in range(len(B)):
        res.append(binery_search(A,B[i])+1)
    return res

A =[3,4,4,6]
B =[20,4,10,2]
print(solve(A,B))