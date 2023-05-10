def solve(A,B):
    hm ={}
    count =0
    for a in A:
        b1 = a - B
        b2 = a + B
        if b1 in hm:
            count += hm[b1]
        if b2 in hm:
            count += hm[b2]

        hm[a] = hm.get(a,0) + 1
    return count

A = [3, 5, 1, 2]
B = 4
A = [1, 2, 1, 2]
B = 1
print(solve(A,B))