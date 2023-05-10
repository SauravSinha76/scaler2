def solve(A,B):

    hm = {}
    count = 0
    for a in A:
        b = B - a
        if b in hm:
            count += hm[b]
        hm[a] = hm.get(a,0) + 1
    return count

A = [3, 5, 1, 2]
B = 8
print(solve(A,B))
