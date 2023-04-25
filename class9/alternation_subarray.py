def validArray(sub):
    i = 0
    j = len(sub)-1
    while i < j:
        if sub[i] != sub[j]:
            return False
        i += 1
        j -= 1
    return True
def solve(A,B):
    n = len(A)
    ans =[]
    for i in range(B, n-B):
        if validArray(A[i-B:i+B+1]):
            ans.append(i)
    return ans

A = [1, 0, 1, 0, 1]
B = 1
# A = [0, 0, 0, 1, 1, 0, 1]
# B = 0
print(solve(A,B))