def binery_serach(A,B):
    l = 0
    r = len(A)-1
    while l < r:
        mid = l + (r - l) // 2

        if A[mid] > B:
            r = mid
        else:
            l = mid + 1
    return l
def solve(A,B):
    for i in range(1,len(A)):
        A[i] += A[i-1]
    res =[]
    for j in range(len(B)):
        res.append(binery_serach(A,B[j]))
    return res
from bisect import bisect_right
def solve1(A,B):
    for i in range(1,len(A)):
        A[i] += A[i-1]

    for i in range(len(B)):
        B[i] = bisect_right(A,B[i])
    return B
A = [3,4,4,6]
B = [20,4,10,2]
print(solve(A,B))
# print(solve1(A,B))