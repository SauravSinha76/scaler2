def solve(A):
    n = len(A)
    seat=[]
    for i in range(n):
        if A[i] == 'x':
            seat.append(i)


    mid = len(seat) // 2

    l = mid -1
    r = mid +1
    k = 1
    res = 0

    while l > -1:
        res += (seat[mid] - seat[l] - k)
        l -= 1
        k += 1

    k = 1
    while r < len(seat):
        res += (seat[r] - seat[mid] - k)
        r += 1
        k += 1

    return res

A = "....x..xx...x.."
print(solve(A))