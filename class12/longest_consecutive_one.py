def solve(A):
    n = len(A)
    count = 0
    for i in range(n):
        if A[i] == '1':
            count += 1
    if count == 0:
        return 0
    if count == n:
        return n
    ans = 0
    for i in range(n):
        if A[i] == '0':
            l = 0
            r = 0
            j = i-1
            while j > -1:
                if A[j] == '1':
                    l += 1
                else:
                    break
                j -= 1
            j = i+1
            while j < n:
                if A[j] == '1':
                    r += 1
                else:
                    break
                j += 1
            k = l+r
            if k < count:
                k += 1
            ans = max(ans,k)
    return ans
A = "111000"
A = "111011101"
print(solve(A))