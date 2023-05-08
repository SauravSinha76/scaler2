def solve(A,B,C):
    ans = 1
    for i in range(B):
        ans = (ans * A) % C

    return ans

A = 2
B = 3
C = 3

A = 5
B = 2
C = 4
print(solve(A,B,C))