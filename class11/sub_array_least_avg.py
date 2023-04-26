def solve(A,B):
    n = len(A)
    sum = 0
    for i in range(B):
        sum += A[i]

    ans = sum
    min_idx = 0
    s = 0
    e = B
    while e < n:
        sum += A[e] - A[s]
        s += 1
        e += 1
        if sum < ans:
            ans = sum
            min_idx = s
    return min_idx

A = [3, 7, 90, 20, 10, 50, 40]
B = 3
print(solve(A,B))