def isPrime(A):
    if A == 1:
        return 0
    i = 2
    while i * i <= A:
        if A % i == 0:
            return 0
        i += 1
    return 1

def solve(A,B):
    for i in range(len(A)):
        A[i] = isPrime(A[i])

    for i in range(1, len(A)):
        A[i] += A[i-1]

    res =[]
    for b in B:
        l = b[0] -1
        r = b[1] -1
        if l == 0:
           res.append(A[r])
        else:
            res.append(A[r] - A[l-1])
    return res

A = [1,4,5,2]
B = [
    [2,3],
    [3,4],
    [1,4]
]
print(solve(A,B))

