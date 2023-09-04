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

def nearest_gratest_left(A):
    n = len(A)
    stack = []
    ans = [-1] * n
    for i in range(n):
        while stack and A[stack[-1]] <= A[i]:
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


def nearest_gratest_right(A):
    n = len(A)
    stack = []
    ans = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()

        if not stack:
            ans[i] = n
        else:
            ans[i] = stack[-1]

        stack.append(i)
    return ans

def solve(A):
    n = len(A)
    nsl = nearest_smallest_left(A)
    ngl = nearest_gratest_left(A)
    nsr = nearest_smallest_right(A)
    ngr = nearest_gratest_right(A)
    max_sum = 0
    min_sum = 0
    for i in range(n):
        max_sum += A[i] *(ngr[i] - i) *(i - ngl[i])
        min_sum += A[i] *(nsr[i] - i) * (i - nsl[i])

    return max_sum - min_sum


A = [4, 5, 2, 10, 8, 2]
print(nearest_smallest_left(A))
print(nearest_gratest_left(A))
print(nearest_smallest_right(A))
print(nearest_gratest_right(A))
print(solve(A))