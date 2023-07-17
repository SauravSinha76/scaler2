def count_smaller(A,B):
    l = 0
    r = len(A) -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == B:
            return mid
        if A[mid] < B:
            l = mid +1
        else:
            r = mid -1
    return l

A = [2,7,10,15,17,20]
print(count_smaller(A,9))
def solve(A,B,K):
    l = min(A[0],B[0])
    r = max(A[-1],B[-1])
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        idx = count_smaller(A, mid)
        idx += count_smaller(B, mid)

        if idx <= K:
            ans = mid
            l = mid + 1
        else:
            r = mid -1
    return ans

A =[3,7,13,25]
B =[2,9,11]
print(solve(A,B,4))