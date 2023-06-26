def solve(A,B):
    n = len(A)

    for i in range(B):
        min_ele = A[i]
        min_idx = i
        for j in range(i+1,n):
            if min_ele > A[j]:
                min_ele = A[j]
                min_idx = j
        A[i],A[min_idx] = A[min_idx],A[i]

    return A[B-1]
A = [2, 1, 4, 3, 2]
B = 3
print(solve(A,B))