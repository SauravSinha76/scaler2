def solve(A,B):
    A.sort()
    n = len(A)
    i = 0
    j = 1
    count = 0
    while j < n:
        k = A[j] - A[i]
        if k == B:
            count += 1
            i += 1
            while i < j and A[i-1] == A[i]:
                i += 1
            j += 1
            while j < n and A[j-1] == A[j]:
                i += 1
        elif k < B:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    return count




A = [1, 5, 3, 4, 2]
B = 3
print(solve(A,B))