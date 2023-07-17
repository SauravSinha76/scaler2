def solve(A,B):
    l = 0
    r = len(A) - 1
    lb = 0
    while l <= r:
        mid = (l + r) // 2

        if A[mid] >= B:
            lb = mid
            r = mid - 1
        else:
            l = mid +1
    ub = 0
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l + r) // 2

        if A[mid] <= B:
            ub = mid
            l = mid +1
        else:
            r = mid - 1
    return ub - lb + 1

A =[-5,-5,-3,0,0,1,1,5,5,5,5,5,5,5,8,10,15,15]
print(solve(A,5))