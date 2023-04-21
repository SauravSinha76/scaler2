def solve(A,B):
    n = len(A)
    count =0
    for i in range(n):
        if A[i] == B:
            count += 1

    return count

A = [1, 2, 2]
B = 2
print(solve(A,B))