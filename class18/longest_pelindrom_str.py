def solve(A):
    n = len(A)
    def expand(p1, p2):
        while p1 > -1 and p2 < n and A[p1] == A[p2]:
            p1 -= 1
            p2 += 1
        return p1+1,p2

    max_length = 0
    max_start =-1
    max_end = -1
    for i in range(n):
        if i != 0:
            s,e = expand(i-1,i)
            if max_length < e - s :
                max_length = e - s
                max_start = s
                max_end = e
        s,e = expand(i,i)
        if max_length < e - s:
            max_length = e - s
            max_start = s
            max_end = e
    return A[max_start:max_end]

A = "aaaabaaa"
A = "abba"
print(solve(A))