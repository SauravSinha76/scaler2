def solve(A,B):
    hm ={}
    hs =set()
    C =[]
    for a in A:
        hm[a] = hm.get(a,0) + 1

    for b in B:
        if b in hm:
            hs.add(b)
            while hm[b] > 0:
                C.append(b)
                hm[b] -= 1
    for a in A:
        if a not in hs:
            C.append(a)
    return C


A = [1, 2, 3, 4, 5, 4]
B = [5,5, 4, 2]
print(solve(A,B))