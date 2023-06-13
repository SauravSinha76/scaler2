def gcd(a,b):
    if b == 0:
        return a

    return gcd(b, a % b)

def solve(A):

    n = len(A)

    pgcd = [0] *n
    sgcd = [0] *n
    pgcd[0] = A[0]
    sgcd[n-1] = A[n-1]

    for i in range(1,n):
        pgcd[i] = gcd(pgcd[i-1],A[i])

    for i in range(n-2,-1,-1):
        sgcd[i] = gcd(sgcd[i+1],A[i])

    max_gcd = 0
    for i in range(n):
        if i == 0:
           gcd_val = sgcd[1]
        elif i == n-1:
            gcd_val = pgcd[n-2]
        else:
            gcd_val = gcd(pgcd[i-1],sgcd[i+1])

        max_gcd = max(max_gcd,gcd_val)

    return max_gcd

A = [12, 15, 18]
A = [5, 15, 30]
print(solve(A))

