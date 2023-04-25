def solve(A,B):
    n = len(A)
    count = 0
    for i in range(n):
        sum =0
        for j in range(i,n):
            sum += A[j]
            if sum < B and (j - i +1) % 2 == 0:
                count += 1
            if sum > B and (j - i +1) % 2 == 1:
                count += 1
    return count

A = [1, 2, 3, 4, 5]
B = 4
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(solve(A,B))