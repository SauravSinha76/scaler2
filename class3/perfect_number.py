def solve(A):
    sum = 0

    i =1

    while i * i <= A:
        sum += i
        second_factor = A // i
        if second_factor != i and second_factor != A:
            sum += second_factor
        i += 1
    if sum == A:
        return 1
    else:
        return 0


A = 4
A = 6
print(solve(A))
