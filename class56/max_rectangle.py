def solve(A):
    row = len(A)
    col = len(A[0])
    i = 0
    max_rect = 0
    while i < row:
        j = 0
        while j < col:
            if i != 0 and A[i][j] != 0:
                A[i][j] += A[i - 1][j]
            j += 1
        arr = A[i]
        n = len(arr)
        stack = []
        nsl = [0] * n

        for k in range(n):
            while stack and arr[stack[-1]] >= arr[k]:
                stack.pop()

            if not stack:
                nsl[k] = -1
            else:
                nsl[k] = stack[-1]

            stack.append(k)

        nsr = [n] * n
        stack = []

        for k in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[k]:
                stack.pop()

            if not stack:
                nsr[k] = n
            else:
                nsr[k] = stack[-1]

            stack.append(k)

        for k in range(n):
            max_rect = max(max_rect, arr[k] * (nsr[k] - nsl[k] - 1))

        i += 1
    return max_rect


A = [[0, 0, 1],
     [0, 1, 1],
     [1, 1, 1]]
A = [[0, 1, 0, 1],
     [1, 0, 1, 0]
     ]
print(solve(A))
