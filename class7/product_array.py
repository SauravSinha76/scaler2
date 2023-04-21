def solve(A):
    n = len(A)

    left =[0] *n
    right =[0]*n

    left[0] = 1
    right[n-1] =1
    for i in range(1,n):
        left[i] = left[i-1] * A[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * A[i+1]

    ans =[]
    for i in range(n):
        ans.append(left[i] * right[i])

    return ans

A = [1, 2, 3, 4, 5]
print(solve(A))

