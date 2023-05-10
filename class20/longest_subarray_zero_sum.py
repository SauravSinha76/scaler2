def solve(A):
    n = len(A)

    hs ={0:-1}
    max_length = 0
    psum = 0
    for i in range(n):
        psum += A[i]
        if psum in hs:
            length = i - hs[psum]
            max_length = max(max_length,length)
        else:
            hs[psum] = i
    return max_length

A = [1, -2, 1, 2]
# A = [3, 2, -1]
print(solve(A))
