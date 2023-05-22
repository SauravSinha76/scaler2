def solve(A,B):

    n = len(A)


    for i in range(1,n):
        if i % 2 != 0:
            A[i] = A[i-1]
        else:
            A[i] += A[i-1]
    ans =[]
    for b in B:
        l = b[0]
        r = b[1]

        if l == 0:
           ans.append(A[r])
        else:
            ans.append(A[r]- A[l-1])

    return ans

A = [1, 2, 3, 4, 5]
B = [   [0,2],
        [1,4]   ]
A = [2, 1, 8, 3, 9]
B = [   [0,3],
        [2,4]   ]
print(solve(A,B))
