def check_bit(num,idx):
    return num & 1 << idx

def solve(A):
    ans =0
    for i in range(32):
        count =0
        for a in A:
            if a & 1 << i:
                count += 1

        if count % 3 == 1:
           ans |= 1 << i
    return ans

A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(solve(A))