def permu(idx,n,temp,visited,A,ans):
    if idx == n:
        ans.append(list(temp))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp[idx] = A[i]
            permu(idx + 1, n,temp,visited,A,ans)
            visited[i] = False


def solve(A):
    n = len(A)
    ans= []
    temp = [0] * n
    visited =[False] * n
    permu(0,n,temp,visited,A,ans)
    return ans


A =[1,2,3,4]
for a in solve(A):
    print(a)