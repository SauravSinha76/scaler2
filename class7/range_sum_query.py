def solve(A,B):
    n = len(A)
    for i in range(1,n):
        A[i] += A[i-1]

    ans = []
    for l,r in B:
        if l ==0:
            ans.append(A[r])
        else:
            ans.append(A[r]-A[l-1])
    return ans

A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
print(solve(A,B))