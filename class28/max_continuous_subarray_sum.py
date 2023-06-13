def solve(A):
    max_sum = 0
    sum = 0
    for a in A:
        sum += a
        max_sum = max(max_sum, sum)
        if sum < 0:
            sum = 0
    return max_sum


def max_sum_sub_array(A):
    max_sum = -(1 << 31)
    curr_sum = 0
    n = len(A)
    start = -1
    end = -1
    s = 0
    for i in range(n):
        curr_sum += A[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i + 1
            start = s
        if curr_sum < 0:
            curr_sum = 0
            s = i + 1
    return A[start:end]


A = [1, 2, 3, 4, -10]
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solve(A))
print(max_sum_sub_array(A))
