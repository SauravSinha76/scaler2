def solve(A):
    n = len(A)
    ans = 0
    for a in A:
        ans ^= a

    idx = -1
    for i in range(31):
        if ans & 1 << i:
            idx = i
            break

    set1 = 0
    set2 = 0

    for a in A:
        if a & 1 << idx:
            set1 ^= a
        else:
            set2 ^= a

    if set1 < set2:
        return [set1,set2]
    else:
        return [set2,set1]


A = [1, 2, 3, 1, 2, 4]
A = [1, 2]
print(solve(A))