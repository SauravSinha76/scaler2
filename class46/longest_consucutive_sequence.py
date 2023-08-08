def solve(A):
    hs = set()

    for a in A:
        hs.add(a)
    ans = 0
    for a in hs:
        if a-1 not in hs:
            chain =1
            y = a+1
            while y in hs:
                y += 1
                chain += 1

            ans = max(ans, chain)
    return ans


A = [100, 4, 200, 1, 3, 2]
print(solve(A))
