def solve(A):
    n = len(A)
    i = n-1

    while i >= 0 and A[i] == 9:
        A[i] = 0
        i -= 1

    if i < 0:
        A.insert(0,1)
    else:
        A[i] += 1

    start =0
    while start < n and A[start] == 0:
        start += 1
    return A[start:]

A = [8, 9, 9]
print(solve(A))