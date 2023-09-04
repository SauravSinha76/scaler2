def solve(A):
    n = len(A)

    for i in range(n-1):
        for j in range(i+2,n+1):
            print(A[i:j])

A =[2, 3, 1, 4]
print(solve(A))