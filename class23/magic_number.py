def sum(A):
    if A == 0:
        return 0
    r = A % 10
    A = A // 10
    return sum(A) + r

def solve(A):
    if A // 10 == 0:
        if A == 1:
            return 1
        else: return 0

    return solve(sum(A))

print(solve(83557))
print(solve(1291))

