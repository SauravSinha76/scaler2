def solve(A):
    n = len(A)
    max_length = 0
    max_l =0
    max_r = n
    for i in range(n):
        if A[i] < 0:
            l = i -1
            while l > -1:
                if A[l] >= 0:
                    l -= 1
                else:
                    break
            if max_length < i - l - 1:
                max_length = i - l - 1
                max_l = l + 1
                max_r = i

            r = i+1
            while r < n:
                if A[r] >= 0:
                    r += 1
                else:
                    break
            if max_length < r - i -1:
                max_length = r - i -1
                max_l = i + 1
                max_r = r
    return A[max_l: max_r]

A = [5, 6, -1, 7, 8]
A = [1, 2, 3, 4, 5, 6]
print(solve(A))