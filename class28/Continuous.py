def solve(A,B):
    ans = [0] * A
    for b in B:
        ans[b[0]-1] += b[2]
        if b[1] < A:
            ans[b[1]] += -b[2]

    print(ans)

    for i in range(1,A):
        ans[i] += ans[i-1]

    return ans

A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(solve(A,B))