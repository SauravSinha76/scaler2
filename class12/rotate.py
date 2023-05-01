def reverse(A,s,e):
    while s < e:
        A[s],A[e] = A[e],A[s]
        s += 1
        e -= 1

def solve(A,B):
    n = len(A)
    res =[]
    for b in B:
        temp = list(A)
        reverse(temp,0,n-1)
        reverse(temp,0,n-b-1)
        reverse(temp,n-b,n-1)
        res.append(temp)
    return res

A = [1, 2, 3, 4, 5]
B = [2, 3]
print(solve(A,B))