def gcd(B,C):
    if C == 0:
        return B
    return gcd(C,B % C)

def lcm(B,C):
    return (B * C) // gcd(B,C)

def count_multiple(B,C,m):
    return m // B + m // C - m // lcm(B,C)

def solve(A,B,C):
    high = min(B,C) * A
    low = min(B,C)
    ans = -1
    while low <= high:
        mid = (high + low) // 2
        count = count_multiple(B,C,mid)
        if count >= A:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans

A = 8
B = 2
C = 3
print(solve(A,B,C))