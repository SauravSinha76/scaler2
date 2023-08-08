def solve(A):
    unique =set()
    pow = 10
    while A > 0:
        n = A
        p = 1
        while n > 0:
            p *= n % pow
            n //= pow
            if p in unique:
                return 0
            unique.add(p)
        A //= pow
    return 1

A = 236
A = 3245
print(solve(A))
