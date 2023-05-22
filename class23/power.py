def pow(a,n):
    print(n)
    if n == 0:
        return 1
    return pow(a,n-1) * a

def pow2(a,n):
    print(n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow2(a ,n // 2) * pow2(a, n // 2)
    else:
        return a *  pow2(a, n// 2) * pow2(a, n // 2)

def pow3(a,n):
    # print(n)
    if n == 0:
        return 1
    p = pow3(a, n // 2)
    if n % 2 == 0:
        return p * p
    else:
        return a * p * p
print(pow(2,100))
print("--------------------")
print(pow2(2,100))
print("--------------------")
print(pow3(2,100))