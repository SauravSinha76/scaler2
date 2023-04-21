def solve(A):
    i = 2
    while i * i <=A:
        if A % i == 0:
            return 0
        i += 1
    return 1

print(solve(10 **9 + 6))