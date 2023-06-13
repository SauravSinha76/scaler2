def solve(A):

    num =[True] * (A+1)

    num[0] = False
    num[1] = False
    i = 2
    while i * i <= A:
        if num[i]:
            for j in range(i*i,A+1,i):
                num[j] = False
        i += 1

    for i in range(A+1):
        if num[i]:
            print(i)



solve(50)