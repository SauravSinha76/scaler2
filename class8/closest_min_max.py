def solve(A):
    n = len(A)

    max_ele = max(A)
    min_ele = min(A)
    if min_ele == max_ele:
        return 1
    mini = -1
    maxi = -1
    ans = 0
    for i in range(n-1,-1,-1):
        if A[i] == max_ele:
            maxi = i
            if mini != -1:
                ans = max(ans,mini - maxi + 1)
        elif A[i] == min_ele:
            mini = i
            if maxi != -1:
                ans = max(ans, maxi - mini + 1)
    return ans

A = [1, 3, 2]
A = [2, 6, 1, 6, 9]
print(solve(A))

