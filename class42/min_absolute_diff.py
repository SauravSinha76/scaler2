def count_smaller(A,B):
    l = 0
    r = len(A) -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == B:
            return mid
        if A[mid] < B:
            l = mid + 1
        else:
            r = mid -1
    return l

def solve(A,B,C):
    for i in range(A):
        C[i].sort()

    ans = 1 << 31

    for i in range(A-1):
        for j in range(B):

            p = count_smaller(C[i+1],C[i][j])

            if p == B:
                p -= 1

            ans = min(ans,abs(C[i+1][p] - C[i][j]))

            if p > 0:
                ans = min(ans, abs(C[i + 1][p-1] - C[i][j]))
    return ans

A = 2
B = 2
C = [ [8, 4],
      [6, 8] ]

A = 3
B = 2
C = [ [7, 3],
       [2, 1],
       [4, 9] ]
print(solve(A,B,C))