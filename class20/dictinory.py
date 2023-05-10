def solve(A,B):
    hm={}
    b = len(B)
    for i in range(b):
        hm[B[i]] = i

    for i in range(1,len(A)):
        min_str_len = min(len(A[i]),len(A[i-1]))
        j =0
        while j < min_str_len:
            if hm[A[i][j]] < hm[A[i-1][j]]:
                return 0
            elif hm[A[i][j]] == hm[A[i-1][j]]:
                j += 1
            else:
                break
        if len(A[i-1]) > len(A[i]):
            return 0
    return 1

A = ["hello", "scaler", "interviewbit"]
B = "adhbcfegskjlponmirqtxwuvzy"
A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"
print(solve(A,B))