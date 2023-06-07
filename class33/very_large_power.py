def power(A,B,C):

    res = 1

    A = A % C

    while B > 0:

        if B & 1:
            res = (res * A) % C


        B = B >> 1
        A = (A * A) % C

    return res