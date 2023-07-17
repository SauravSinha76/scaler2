def count_student(A,pages):
    pages_left = pages
    count = 1
    for a in A:
        if a > pages:
            return -1
        if a <= pages_left:
            pages_left -= a
        else:
            count += 1
            pages_left = pages - a

    return count

def solve(A,B):
    low = max(A)
    high = sum(A)
    ans = -1

    while low <= high:
        mid = (high + low) // 2

        student = count_student(A,mid)

        if student <= B:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

A = [12, 34, 67, 90]
B = 2
print(solve(A,B))