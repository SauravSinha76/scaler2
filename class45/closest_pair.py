def solve(A,B,C):
    n = len(A)
    m = len(B)
    ans =[-1,-1]
    min_diff = (1<<31) -1
    for i in range(n):
        for j in range(m):
            diff = abs(C - (A[i] + B[j]))
            if diff < min_diff:
                min_diff = diff
                ans[0] = A[i]
                ans[1] = B[j]
    return ans

def solve1(A,B,C):
    n = len(A)
    m = len(B)
    ans =[-1,-1]
    min_diff = (1<<31) -1
    i = 0
    j = m-1
    while i < n and j > -1:
        sum = A[i] + B[j]
        diff = abs(C - sum)
        if min_diff > diff:
            ans[0] = i
            ans[1] = j
            min_diff = diff
        elif min_diff == diff and ans[0] > i and ans[1] > j:
            ans[0] = i
            ans[1] = j
        if sum < C:
            i += 1
        else:
            j -= 1

    return [A[ans[0]],B[ans[1]]]
A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8]
C = 9
# A = [5, 10, 20]
# B = [1, 2, 30]
# C = 13
print(solve(A,B,C))
print(solve1(A,B,C))