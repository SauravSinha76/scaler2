def solve(A):
    hash_map ={}

    for a in A:
        hash_map[a] = hash_map.get(a,0) + 1

    for a in A:
        if hash_map[a] > 1:
            return a
    return -1

A = [10, 5, 3, 4, 3, 5, 6]
A = [6, 10, 5, 4, 9, 120]
print(solve(A))