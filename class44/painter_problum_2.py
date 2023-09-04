def count_painter(C,B,mid):
    time = mid
    count =1
    for i in range(len(C)):
        if C[i] * B > mid:
            return -1
        if C[i] * B <= mid:
            time -= C[i] * B
        else:
            count += 1
            time = mid - C[i] * B
    return count


def solve(A,B,C):
    l = max(C) * B
    r = sum(C) * B
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        painter = count_painter(C,B,mid)

        if painter <= A:
           ans = mid
           r = mid - 1
        else:
            l = mid +1

    return ans






A = 10
B = 1
C = [1, 8, 11, 3]

A = 2
B = 5
C = [1, 10]
print(solve(A,B,C))