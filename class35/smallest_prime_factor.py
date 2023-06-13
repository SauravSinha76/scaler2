def solve(A):

    num = [i for i in range(A+1)]

    i = 2
    while i * i <= A:
        if num[i] == i:
            for j in range(i*i , A+1, i):
                num[j] = i
        i += 1
    for i in range(A+1):
        print(f"{i} smallest prime factor {num[i]}")


print(solve(50))