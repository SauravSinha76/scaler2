def solve_brt(A,B):
    n = len(A)
    m = len(B)
    count =0
    for i in range(n):
        for j in range(m):
            if A[i] > B[j]:
                count += 1
    return count


def solve(A,B):
    n = len(A)
    m = len(B)

    count = 0
    i =0
    j =0

    while i < n and j < m:
        if A[i] <= B[j]:
            i += 1
        else:
            count += (n-i)
            j += 1
    return count
A = [3,6,8,10,15]
B = [1,2,7,12,18]
print(solve_brt(A,B))
print(solve(A,B))