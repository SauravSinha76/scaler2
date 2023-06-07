def divide( A, B):
    sign = -1 if (A < 0) ^ (B < 0) else 1

    dividend = abs(A)
    divisor = abs(B)

    qua = 0
    temp = 0

    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            qua |= 1 << i

    qua *= sign

    if qua > (1 << 31) - 1:
        return (1 << 31) - 1
    return qua


print(divide(35,7))