def solve(A):
    n = len(A)
    ele = A[0]
    freq = 1
    for i in range(1,n):
        if freq == 0:
            ele = A[i]
        elif ele == A[i]:
            freq += 1
        else:
            freq -= 1

    if freq > 0:
        return ele

    count =0
    for i in range(n):
        if ele == A[i]:
            count += 1

    if count >= n // 2:
        return ele


A =[2, 1, 2]
print(solve(A))


