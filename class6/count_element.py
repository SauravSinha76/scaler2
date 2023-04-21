def solve(A):
    n = len(A)
    max_ele = A[0]
    for i in range(1,n):
        if max_ele < A[i]:
            max_ele = A[i]
    c = 0
    for i in range(n):
        if A[i] == max_ele:
            c += 1

    return n -c

def solve2(A):
    n = len(A)
    max_ele = A[0]
    count = 0
    temp =0
    for i in range(1,n):
        if A[i] < max_ele:
            count += 1
        elif max_ele < A[i]:
            max_ele = A[i]
            count += (temp +1)
            temp = 0
        else:
            temp += 1
    return count
A = [3, 1, 2]
A = [5, 5, 3]
print(solve(A))
print(solve2(A))