def solve(A,B):
    n= len(A)
    k = 0
    for i in range(n):
        if A[i] <= B:
            k += 1

    bad =0
    for i in range(k):
        if A[i] > B:
            bad += 1

    ans = bad
    s = 0
    e = k
    while e < n:
        if A[s] > B:
            bad -= 1
        if A[e] > B:
            bad += 1
        ans = min(ans,bad)
        e += 1
        s += 1
    return ans

A = [1, 12, 10, 3, 14, 10, 5]
B = 8
A = [5, 17, 100, 11]
B = 20
print(solve(A,B))
