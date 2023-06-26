def solve(A):
    n = len(A)

    for i in range(n):
        min_ele = A[i]
        min_idx = i
        for j in range(i+1,n):
            if A[j] < min_ele:
                min_ele = A[j]
                min_idx = j

        A[i],A[min_idx] = A[min_idx],A[i]
    return A

A =[9,3,3,-4,5,1,6,7,-2,11,4,5]
print(solve(A))