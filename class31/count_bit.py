def solve(A):
    count =0
    for i in range(32):
        if A & 1<< i:
            count += 1
    return count

A = 1
print(solve(A))