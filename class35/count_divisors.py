def get_spf(A):
    spf = [i for i in range(A+1)]

    i = 2
    while i * i <= A:
        if spf[i] == i:
            for j in range(i*i, A+1, i):
                spf[j] = i
        i += 1
    return spf


def solve(A):

    max_num = max(A)

    spf = get_spf(max_num)
    ans =[]
    for a in A:
        x = a
        count = 1
        l =[]
        while x > 1:
            l.append(spf[x])
            x //= spf[x]

            count += 1
        ans.append(count)
        print(l)
    return ans

A = [2, 3, 4, 5]
A = [8, 9, 10]
print(solve(A))
