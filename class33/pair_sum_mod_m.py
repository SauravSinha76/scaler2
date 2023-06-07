def solve(A,B):

    hm={}

    for a in A:
        idx = a % B
        hm[idx] = hm.get(idx,0) + 1

    ans = 0

    x = hm.get(0,0)
    ans += (x*(x-1))//2
    if B % 2 ==0:
        x = hm.get(B//2,0)
        ans += (x * (x - 1)) // 2

    for i in range(1,(B+1)//2):
        ans += hm.get(i,0) * hm.get(B-i,0)

    return ans


A = [1, 2, 3, 4, 5]
B = 2

A = [5, 17, 100, 11]
B = 28
print(solve(A,B))