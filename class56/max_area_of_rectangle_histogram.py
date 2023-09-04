def nearest_smallest_left(A):
    n = len(A)
    stack = []
    ans = [-1] * n
    for i in range(n):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()

        if not stack:
            ans[i] = -1
        else:
            ans[i] = stack[-1]

        stack.append(i)
    return ans


def nearest_smallest_right(A):
    n = len(A)
    stack = []
    ans = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()

        if not stack:
            ans[i] = n
        else:
            ans[i] = stack[-1]

        stack.append(i)
    return ans

def solve(A):
    nsl = nearest_smallest_left(A)
    nsr = nearest_smallest_right(A)

    n = len(A)
    max_area = 0
    for i in range(n):
        max_area = max(max_area, A[i] * (nsr[i] - nsl[i] - 1))

    return max_area

A = [4, 5, 2, 10, 8, 2]
print(nearest_smallest_left(A))
print(nearest_smallest_right(A))
print(solve(A))
