def solve(A,B):
    n = len(A)
    sum =0
    start = 0
    for i in range(n):
        sum += A[i]
        end = i+1
        while sum > B:
            sum -= A[start]
            start += 1
        if sum == B:
            return A[start: end]
    return [-1]

def solve1(A,B):
    n = len(A)
    hm = {0:-1}
    psum =0
    for i in range(n):
        psum += A[i]
        a = psum
        b = a - B
        if b in hm:
            return A[hm[b]+1:i+1]
        hm[a] = i
    return [-1]



A = [1, 2, 3, 4, 5]
B = 5
# A = [5, 10, 20, 100, 105]
# B = 110
print(solve(A,B))
print(solve1(A,B))