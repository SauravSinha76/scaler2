def solve(A):
    n = len(A)
    i = 0
    j = n-1
    max_water = 0
    while i < j:
        water = min(A[i],A[j]) *(j - i)
        max_water = max(max_water,water)
        if A[i] < A[j]:
            i += 1
        else:
            j -= 1
    return max_water
A = [1, 5, 4, 3]
print(solve(A))