def solve(A):
    A.sort()
    sum = 0
    n = len(A)
    for i in range(n):
        sum += A[i]* ((1 << i) - (1 << (n-i-1)))
    return sum

A = [1,2]
A =[3,5,10]
A = [3,1,-4]
print(solve(A))