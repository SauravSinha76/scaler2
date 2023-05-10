def solve(A,B):
    hm ={}

    n = len(A)
    ans =[]
    for i in range(B):
        hm[A[i]] = hm.get(A[i],0) + 1
    ans.append(len(hm))

    s = 0
    e = B

    while e < n:
        if hm[A[s]] > 1:
            hm[A[s]] -= 1
        else:
            hm.pop(A[s])

        hm[A[e]] = hm.get(A[e],0) + 1
        ans.append(len(hm))
        e += 1
        s += 1
    return ans

A = [1, 2, 1, 3, 4, 3]
B = 3
A = [1, 1, 2, 2]
B = 1
print(solve(A,B))
