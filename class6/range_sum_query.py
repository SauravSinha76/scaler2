def solve(A,B):
    ans =[]
    for b in B:
        sum =0
        for i in range(b[0],b[1]+1):
            sum += A[i]
        ans.append(sum)

    return ans

def solve2(A,B):
    n = len(A)
    for i in range(1,n):
        A[i] += A[i-1]
    ans =[]
    for b in B:
        l = b[0]
        r = b[1]
        if l ==0:
           ans.append(A[r])
        else:
            ans.append(A[r] - A[l-1])
    return ans
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
print(solve(A,B))
print(solve(A,B))