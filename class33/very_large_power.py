def power(A, B, C):
    res = 1

    A = A % C

    while B > 0:

        if B & 1:
            res = (A * A) % C

        C = C >> 1
        A = (A * A) % C

    return res


def pow(A,B,C):
    if A == 0:
        return 0
    if B == 0:
        return 1

    p = pow(A,B//2,C)
    x = (p * p) % C

    if B % 2 == 0:
        return x
    else:
        return (A * x) % C

