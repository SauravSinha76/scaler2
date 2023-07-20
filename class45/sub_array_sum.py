def solve(A,B):
    n = len(A)
    psum=[0,A[0]]

    for i in range(1,n):
        psum.append(psum[i] +A[i])

    i = 0
    j = 1
    while j < n+1:
        diff = psum[j] - psum[i]
        if diff == B:
            return A[i:j]
        elif diff < B:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    return [-1]

A = [1, 2, 3, 4, 5]
B = 5
print(solve(A,B))