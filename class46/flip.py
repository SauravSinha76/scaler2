def celeing(A,idx):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == idx:
            return mid
        if A[mid] < idx:
            l = mid + 1
        else:
            r = mid - 1
    return l

def solve(A,B):
    index =[]
    for i in range(len(A)):
        if A[i] == '1':
            index.append(i+1)

    print(index)
    ans = []
    for b in B:
        type = b[0]
        idx = b[1]
        if type == 1:
            if idx in index:
                index.remove(idx)
            else:
                index.append(idx)
        else:
            index.sort()
            right = celeing(index,idx)
            left = right - 1

            if right >= len(index) and left < 0:
                ans.append(-1)
            if right < len(index) and left < 0:
                ans.append(index[right])
            elif right >= len(index) and left >= 0:
                ans.append(index[left])
            else:
                if index[right] - idx < idx - index[left]:
                    ans.append(index[right])
                else:
                    ans.append(index[left])

    return ans


A = "10110"
B = [[1, 2],
     [2, 3]]
# A = "010000100"
# B = [[2, 5],
#      [1, 7],
#      [2, 12]]
print(solve(A,B))