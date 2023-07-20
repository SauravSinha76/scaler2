def check(A,mid):
    last_pos = A[0]
    n = len(A)
    count = 1
    for i in range(1,n):
        if A[i] - last_pos >= mid:
            last_pos = A[i]
            count += 1
    return count

def solve(A,B):
    A.sort()
    left = 1
    right = A[-1] - A[0]
    ans = -1
    while left <= right:
        mid = (left + right) // 2

        cows = check(A,mid)

        if cows >= B:
            ans = mid
            left = mid + 1
        else:
            right= mid - 1
    return ans


A = [1, 2, 3, 4, 5]
B = 3
print(solve(A,B))