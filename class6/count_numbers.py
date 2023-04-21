def solve(A):
    n = len(A)
    max_num = max(A)
    count =0
    for i in range(n):
        if max_num > A[i]:
            count += 1
    return count

A = [3, 1, 2]
A = [5, 5, 3]
print(solve(A))