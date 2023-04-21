def solve(A,B):
    n = len(A)

    for i in range(n):
        if A[i] % 2 == 0:
            A[i] = 1
        else:
            A[i] =0
        if i != 0:
            A[i] += A[i - 1]
    ans =[]
    for l,r in B:
        if l ==0:
           ans.append(A[r])
        else:
            ans.append(A[r]- A[l-1])
    return ans

A = [1, 2, 3, 4, 5]
B = [[0, 2],
         [2, 4],
         [1, 4]]

print(solve(A,B))