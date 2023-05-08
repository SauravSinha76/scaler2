def solve(A,B):
    map = {}
    for a in A:
        map[a] = map.get(a,0) + 1

    ans =[]
    for b in B:
        ans.append(map.get(b,0))
    return ans

A = [1, 2, 1, 1]
B = [1, 2,3]
print(solve(A,B))