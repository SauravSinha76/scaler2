def count_cows(A,mid):
    last_pos = A[0]
    count =1
    for i in range(1,len(A)):
        if last_pos + mid <= A[i]:
            last_pos = A[i]
            count += 1
    return count
def solve(A,B):
    l = 1
    r = A[-1] - A[0]
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        cow = count_cows(A,mid)

        if cow >= B:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans

A = [1, 2, 3, 4, 5]
B = 3
print(solve(A,B))