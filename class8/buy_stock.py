def solve(A):
    n = len(A)
    min_ele = A[0]
    max_profit = 0
    for i in range(1,n):
        if min_ele > A[i]:
            min_ele = A[i]
        else:
            max_profit = max(max_profit , A[i] - min_ele)
    return max_profit
A = [1, 4, 5, 2, 4]
print(solve(A))