def solve(A):
    ans =0
    n = len(A)
    for i in range(32):
        count = 0
        for a in A:
            if a & 1 << i:
                count += 1

        ans += (count *( n- count) * 2)
    return ans

A = [2,7]
print(solve(A))