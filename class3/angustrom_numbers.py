def is_angustrom(A):
    temp = A
    total = 0
    while temp > 0:
        remd = temp % 10
        temp = temp // 10
        total += remd ** 3
    if total == A:
        return 1
    else:
        return 0

def solve(A):

    num =[]
    for i in range(1,A+1):
        if is_angustrom(i):
            num.append(i)
    return num

print(solve(200))