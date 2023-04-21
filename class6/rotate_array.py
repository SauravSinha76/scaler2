def reverse(A,i,j):
    while i < j:
        A[i],A[j] = A[j], A[i]
        i += 1
        j -= 1
    return A
def solve(A,B):
    n = len(A)
    B = B % n

    reverse(A,0,n-1)
    reverse(A,0,B-1)
    reverse(A,B,n-1)

    return A

A = [1, 2, 3, 4]
B = 2
print(solve(A,B))
