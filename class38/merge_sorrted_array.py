def solve(A,B):
    i =0
    j =0
    C =[]
    n = len(A)
    m = len(B)
    while i < n and j < m:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < n:
        C.append(A[i])
        i += 1

    while j < m:
        C.append(B[j])
        j += 1

    return C

A = [4, 7, 9]
B = [2, 11, 19]
print(solve(A,B))