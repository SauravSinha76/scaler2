def solve(A):
    n = len(A)
    hash_map ={}
    for i in range(1,n):
        A[i] += A[i-1]

    for a in A:
        if a == 0:
            return 1
        hash_map[a] = hash_map.get(a,0) + 1

    if len(hash_map) < n:
        return 1
    return 0

A = [1, 2, 3, 4, 5]
A = [-1, 1]
print(solve(A))