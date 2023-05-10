def solve(A,B):
    hs = set()
    for b in B:
        a = A - b
        if a in hs:
            return 1
        hs.add(b)
    return 0

A = 8
B = [3, 5, 1, 2, 1, 2]
A = 21
B = [9, 10, 7, 10, 9, 1, 5, 1, 5]
print(solve(A,B))