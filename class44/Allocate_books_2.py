def count_student(A,mid):
    pages = mid
    count = 1
    for i in range(len(A)):
        if A[i] > mid:
            return -1
        if A[i] <= pages:
            pages -= A[i]
        else:
            count += 1
            pages = mid - A[i]
    return count

def solve(A,B):
    l = max(A)
    r = sum(A)
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        stud = count_student(A,mid)

        if stud <= B:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans





A = [12, 34, 67, 90]
B = 2
print(solve(A,B))