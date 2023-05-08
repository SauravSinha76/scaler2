def solve(A,B):
    n = len(A)

    count_A = [0] * 26
    count_B = [0] * 26

    for i in range(n):
        count_A[ord(A[i]) - ord('a')] += 1
        count_B[ord(B[i]) - ord('a')] += 1

    for i in range(26):
        if count_B[i] != count_A[i]:
            return 0
    return 1

A = "cat"
B = "bat"
A = "secure"
B = "rescue"
print(solve(A,B))