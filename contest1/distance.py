def solve(A):
    max_dist =0
    dis =0
    last_index = -1
    for i in range(31):
        if A >> i & 1:
            if last_index != -1:
                dis = i - last_index
            max_dist = max(max_dist,dis)
            last_index = i
    return max_dist

A = 11
print(solve(A))
