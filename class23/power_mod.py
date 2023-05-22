def solve(A,n,m):
    if n == 0:
        return 1

    p = solve(A,n//2,m)
    x = (p * p) % m
    if n % 2 == 0:
        return x
    else:
        return (x * A) % m


print(solve(2,10,7))