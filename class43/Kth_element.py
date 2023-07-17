def count_smaller(A,B):
    count = 0
    for a in A:
        if a < B:
            count += 1
    return count

def solve(A,B):
    l = min(A)
    r = max(A)
    ans = -1
    while l <= r:

        mid = (l + r) // 2

        idx = count_smaller(A,mid)

        if idx <= B:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

A =[2,8,3,11,14]
print(solve(A,2))


