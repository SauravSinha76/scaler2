def solve(A,B):
    hs = set()
    for a in A:
        b1 = a - B
        b2 = a + B

        if b1 in hs:
            return 1
        if b2 in hs:
            return 1

        hs.add(a)
    return 0

A = [5, 10, 3, 2, 50, 80]
B = 78
A = [-10, 20]
B = 30
print(solve(A,B))
