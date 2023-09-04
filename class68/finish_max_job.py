def solve(A,B):
    n = len(A)

    pair=[]
    for i in range(n):
        pair.append((A[i],B[i]))

    pair.sort(key= lambda x:x[1])

    count=1
    lastEnd = pair[0][1]
    for i in range(1,n):
        if lastEnd <= pair[i][0]:
            count += 1
            lastEnd = pair[i][1]

    return count


A = [1, 5, 7, 1]
B = [7, 8, 8, 8]
A = [3, 2, 6]
B = [9, 8, 9]

print(solve(A,B))