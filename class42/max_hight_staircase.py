def solve(A):

    i = 0

    while (i*(i+1))// 2 <= A:
        i += 1

    return i-1

print(solve(10))