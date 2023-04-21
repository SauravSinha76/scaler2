def solve(A):
    n = len(A)
    i =0
    j = n-1
    while i < j:
        A[i],A[j] = A[j],A[i]
        i += 1
        j -= 1

    return A
A = [1,1,10]
print(solve(A))