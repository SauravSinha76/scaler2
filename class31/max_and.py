def checkBit(arr,bit):
    count = 0
    for a in arr:
        if a & 1 << bit:
            count += 1
    return count

def convert_binery(A):
    res = ''
    while A  > 0:
        r =A % 2
        A //= 2
        res = str(r) + res
    return res
def solve(A):
    res = 0
    for bit in range(32,-1,-1):
        count = checkBit(A,bit)

        if count >= 4:
            res |= 1 << bit

            for i in range(len(A)):
                if not (A[i] & 1 << bit):
                    A[i] = 0


    return res


A =[10,20,15,4,14]
A =[2,2,7,15]
A= [1,18,15,16,7,127,3,83,31,23,31]
for a in A:
    print(convert_binery(a).zfill(7))
print(solve(A))