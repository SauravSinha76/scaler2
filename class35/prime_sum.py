def prime(A):
    prime =[True] *(A+1)
    prime[0] = False
    prime[1] = False
    i = 2
    while i * i <= A:
        if prime[i]:
            for j in range(i*i , A+1, i):
                prime[j] = False
        i += 1
    return prime

def solve(A):
    prime_val = prime(A)
    for i in range(A):
        if prime_val[i] and prime_val[A-i]:
            return [i,A-i]


print(solve(11))