def get_spf(A):
    spf = [i for i in range(A+1)]

    i = 2

    while i* i <= A:
        if spf[i] == i:
            for j in range(i*i, A+1, i):
                spf[j] = i
        i += 1
    return spf

def solve(A):
    spf = get_spf(A)

    count=0
    for a in range(A+1):
        l = set()
        while a > 1:
            l.add(spf[a])
            a //= spf[a]

        if len(l) == 2:
            count += 1
    return count

print(solve(12))