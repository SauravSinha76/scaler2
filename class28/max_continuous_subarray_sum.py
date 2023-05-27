def solve(A):
    max_sum = 0
    sum = 0
    for a in A:
        sum += a
        max_sum = max(max_sum,sum)
        if sum < 0:
            sum = 0
    return max_sum

def max_sum_sub_array(A):
    max_sum = -(1 << 31)
    sum = 0
    n = len(A)
    start = -1
    end = -1
    s = 0
    for i in range(n):
        sum += A[i]
        if sum > max_sum:
            max_sum = sum
            end = i+1
            start = s
        if sum < 0:
            sum = 0
            s = i+1
    return A[start:end]
A = [1, 2, 3, 4, -10]
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solve(A))
print(max_sum_sub_array(A))