def solve(A):
    n = len(A)
    totalsubarray = n * (n + 1) // 2
    sum = 0
    max_ele = max(A)
    pos = -1
    for i in range(31, -1, -1):
        if max_ele & 1 << i:
            pos = i + 1
            break

    for i in range(pos):
        v = []
        for j in range(n):
            if not (A[j] & 1 << i):
                v.append(j)
        totalcnt = 0
        cnt = 1
        for j in range(1, len(v)):
            x = v[j] - v[j - 1]

            if x == 1:
                cnt += 1
            else:
                totalcnt += (cnt * (cnt + 1)) // 2
                cnt = 1
        totalcnt += (cnt * (cnt + 1)) // 2
        sum += (1 << i) * (totalsubarray - totalcnt)
    return sum % (10 ** 9 + 7)

A = [1, 2, 3, 4, 5]
print(solve(A))