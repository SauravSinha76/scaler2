def solve(A,B):
    n = len(A)

    count =[0]* 26
    ans = 0
    for i in range(n):
        count[ord(A[i]) - ord('a')] += 1
        if count[ord(A[i]) - ord('a')] == 1:
            ans += 1

    count.sort()

    for i in range(26):
        if count[i] != 0 and B - count[i] >= 0:
            B -= count[i]
            ans -= 1

    return ans

A = "abcabbccd"
B = 3
print(solve(A,B))