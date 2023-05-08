def solve(A):
    n = len(A)
    A.sort(reverse=True)
    greater = -1
    ans = 0
    if A[0] == 0:
        return  1

    for i in range(1,n):
        if A[i] != A[i-1]:
            greater = i
        if A[i] == greater:
            return 1

    return -1

A = [3, 2, 1, 3]
A = [1, 1, 3, 3]
print(solve(A))