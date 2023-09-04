def nearest_small_left(A):
    n = len(A)
    stack =[]
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

def nearest_small_right(A):
    n = len(A)
    stack =[]
    ans =[n] * n
    for i in range(n-1,-1,-1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()

        if not stack:
            ans[i] = n
        else:
            ans[i] = stack[-1]

        stack.append(i)
    return ans

def solve(A):
    n = len(A)
    nsl = nearest_small_left(A)
    nsr = nearest_small_right(A)

    max_rec = 0
    for i in range(n):
        max_rec = max(max_rec, A[i]*(nsr[i] - nsl[i] - 1))

    return max_rec

A = [2, 1, 5, 6, 2, 3]
print(nearest_small_left(A))
print(nearest_small_right(A))
print(solve(A))

