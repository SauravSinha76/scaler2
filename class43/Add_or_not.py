def solve(A,B):
    A.sort()
    n = len(A)
    ans =[-1,-1]
    for i in range(n-1,-1,-1):
        x = B
        count =0
        j = i
        while A[i] - A[j] <= x and j > -1:
            x -= (A[i] - A[j])
            j -= 1
            count += 1
        if count > ans[0]:
            ans[0] = count
            ans[1] = A[i]
    return ans

def optimize(A,B):
    A.sort()
    n = len(A)
    ans =[-1,-1]
    psum= [0,A[0]]
    for i in range(1,n):
        psum.append(A[i] + psum[i])

    for i in range(n):
        low = 0
        high = i
        count =0
        while low <= high:
            mid = (low + high) // 2
            if A[i] * (i - mid + 1) - (psum[i+1] - psum[mid]) <= B:
                count = i - mid + 1
                high = mid -1
            else:
                low = mid + 1

        if count > ans[0]:
            ans[0] = count
            ans[1] = A[i]
    return ans
A =[3,1,2,2,1]
B = 3
print(solve(A,B))
print(optimize(A,B))