def solve(A):
    n = len(A)

    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A

A =[9,3,3,-4,5,1,6,7,-2,11,4,5]
print(solve(A))