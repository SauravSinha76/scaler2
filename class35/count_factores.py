def get_spf(A):
    spf = [i for i in range(A+1)]

    i = 2

    while i * i <= A:
        if spf[i] == i:
            for j in range(i*i, A+1, i):
                spf[j] =i
        i += 1

    return spf

def solve(A):
    max_val = max(A)
    spf = get_spf(max_val)
    res =[]
    for a in A:
        x = a
        l ={}
        while x > 1:
            l[spf[x]] = l.get(spf[x],0) + 1
            x //= spf[x]
        print(l)
        total =1
        for x in l:
            total *= (l[x]+1)
        res.append(total)
    return res

A = [8, 9, 10]
print(solve(A))