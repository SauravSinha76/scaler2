def squ_root(A):
    i = 0
    while i * i <= A:
        if i * i == A:
            return i
        i += 1
    return -1
def solve(A):

    l = 0
    r = A
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        if mid * mid <= A:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans

print(squ_root(64))
print(solve(64))