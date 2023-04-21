def solve(A):
    count = 0
    i = 1
    while i * i <= A:
        if A % i == 0:
            if i != A//i:
                count += 2
            else:
                count += 1
        i += 1
    return count

print(solve(16))