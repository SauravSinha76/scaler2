def solve(A,B):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(n):
            if A[i] * A[j] < B:
                count += 1
    return count

def solve1(A,B):
    n = len(A)
    i = 0
    j = n-1
    count = 0
    while i <= j:
        area = A[i] * A[j]
        if area > B:
            j -= 1
        else:
            count += 2 * (j - i) + 1
            i += 1
    return count % (10 ** 9 +7)

A = [1, 2]
B = 5
# A = [1, 2]
# B = 1
print(solve(A,B))
print(solve1(A,B))