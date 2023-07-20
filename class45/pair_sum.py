def solve(A,B):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] + A[j] == B:
                count += 1
    return count

def solve1(A,B):
    n =len(A)
    hash = {}
    count = 0
    for i in range(n):
        b = B - A[i]
        if b in hash:
            count += hash[b]
        hash[A[i]] = hash.get(A[i],0) + 1

    return count

def solve2(A,B):
    A.sort()
    n = len(A)
    i =0
    j = n-1
    count = 0
    while i < j:
        k = A[i] + A[j]
        if k == B:
            count += 1
            i += 1
            j -= 1
        elif k < B:
            i += 1
        else:
            j -= 1
    return count

def solve3(A,B):
    n = len(A)
    i = 0
    j = n-1
    count =0
    while i < j:
        add = A[i] + A[j]
        if add < B:
            i += 1
        elif add > B:
            j -= 1
        else:
            if A[i] == A[j]:
                x = j - i + 1
                count += (x*(x-1)) // 2
                i,j=j,i
            else:
                left_count =0
                while i < j and A[i] == A[i+1]:
                    left_count += 1
                    i += 1
                right_count =0
                while j > i and A[j] == A[j-1]:
                    right_count += 1
                    j += 1
                count += right_count * left_count
            i += 1
            j -= 1
    return count


A = [1, 2, 3, 4, 5]
B = 5
A = [1, 1, 1] 
B = 2
A = [1, 1, 1,2,2,2,2,2,1,1,1]
B = 4
print(solve(A,B))
print(solve1(A,B))
print(solve2(A,B))
print(solve3(A,B))