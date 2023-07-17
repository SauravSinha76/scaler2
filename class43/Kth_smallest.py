def count_smaller(A,B):
    low = 0
    high = len(A)

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == B:
            return mid
        if A[mid] < B:
            low = mid + 1
        else:
            high = mid -1
    return low
def brut_force(A,B):

    n = len(A)
    C =[]
    for i in range(1,n-1):
        for j in range(i):
            for k in range(i+1,n):
                C.append(A[j]+A[i]+A[k])

    C.sort()


    return C[B]

def position(A,mid):
    count =0
    n = len(A)

    for i in range(n):
        s = i+1
        e = n-1
        while s < e:
            if A[i] + A[s] + A[e] < mid:
                count += e - s
                s += 1
            else:
                e -= 1
    return count

def optimized(A,B):
    n = len(A)
    A.sort()

    max_val = A[n-1] + A[n-2] + A[n-3]
    min_val = A[0] + A[1] + A[2]
    ans =-1
    while min_val <= max_val:
        mid = (max_val + min_val) // 2
        pos = position(A,mid)

        if pos <= B:
           ans = mid
           min_val = mid + 1
        else:
            max_val = mid - 1
    return ans

A =[2,4,3,2]
B = 3
print(brut_force(A,B))
print(optimized(A,B))
