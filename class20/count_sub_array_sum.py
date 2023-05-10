def solve(A,B):
    n = len(A)
    hm = {0:1}
    psum = 0
    count =0
    for i in range(n):
        psum += A[i]
        a = psum
        b = a - B
        if b in hm:
            count += hm[b]
        hm[a] = hm.get(a,0) + 1
    return count

A = [1, 0, 1]
B = 1
print(solve(A,B))