def solve(A,B):
    hm = {}
    count =0
    for a in A:
        b = B ^ a

        if b in hm:
            count += hm[b]

        hm[a] = hm.get(a,0) + 1
    return count
A = [5, 4, 10, 15, 7, 6]
B = 5
A = [3, 6, 8, 10, 15, 50]
B = 5
print(solve(A,B))