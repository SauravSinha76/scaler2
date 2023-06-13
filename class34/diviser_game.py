def gcd(a,b):
    if b ==0:
        return a
    return gcd(b, a% b)

def solve(A,B,C):

    lcm = B*C / gcd(B,C)

    val = lcm
    count = 0
    i = 2
    while val <= A:
        val = i * lcm
        i += 1
        count += 1
    return count

A = 12
B = 2
C = 3
print(solve(A,B,C))