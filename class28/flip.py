def solve(A):
    n = len(A)

    v = [0]* n
    for i in range(n):
        if A[i] == '1':
            v[i] = -1
        else:
            v[i] = 1


    curr_sum = 0
    max_sum = 0
    start = -1
    end = -1
    s = 0
    for i in range(n):
        curr_sum += v[i]
        if max_sum < curr_sum:
            max_sum = curr_sum
            end = i
            start = s
        elif curr_sum < 0:
            s = i+1
    if start == -1:
        return []
    return [start,end+1]

A = "010"
# A = "111"
print(solve(A))
