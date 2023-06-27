def solve(A):
    res =[]
    n = len(A)
    j = n // 2
    i =0
    k =0
    while k < n:
        if k % 2 == 0:
            res.append(A[i])
            i += 1
        else:
            res.append(A[j])
            j += 1
        k += 1
    return res





A =[1,3,-2,-6]
print(solve(A))