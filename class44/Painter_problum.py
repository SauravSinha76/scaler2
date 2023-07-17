def painter_required(A,t,mid):
    count =1
    time_taken = mid
    for a in A:
        if a * t > mid:
            return -1
        if a * t <= time_taken:
            time_taken -= a * t
        else:
            count += 1
            time_taken = mid - a * t

    return count


def solve(A,B,C):
    low = max(C) * B
    high = sum(C) * B
    ans = 0
    while low <= high:

        mid = (low + high) // 2

        painter = painter_required(C,B,mid)

        if painter >= A:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


A = 2
B = 5
C = [1, 10]
print(solve(A,B,C))
