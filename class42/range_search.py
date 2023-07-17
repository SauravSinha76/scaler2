def solve(A,B):
    n = len(A)
    l = 0
    r = n -1
    lb =-1
    rb = -1
    while l <= r:
        mid = (l + r) // 2

        if A[mid] >= B:
           lb = mid
           r = mid -1
        else:
            l = mid + 1

    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2

        if A[mid] <= B:
            rb = mid
            l = mid + 1
        else:
            r = mid -1
    return [lb,rb]

A = [5, 7, 7, 8, 8, 10]
B = 8
print(solve(A,B))