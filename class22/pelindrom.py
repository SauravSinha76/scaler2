def isPelindrom(A,s,e):
    if s > e:
        return True
    if A[s] == A[e] and isPelindrom(A,s+1,e-1):
        return True
    return False

def solve(A):
    return isPelindrom(A,0,len(A)-1)

print(solve("madam"))
print(solve("saurav"))