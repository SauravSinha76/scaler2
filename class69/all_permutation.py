def solve(idx,n,temp,visited,A,ans):

    if idx == n:
        ans.append(list(temp))
        return

    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            temp[idx] =A[i]
            solve(idx + 1, n,temp,visited,A,ans)

            visited[i] = False

A ="abc"
n = len(A)
temp =['' for _ in range(n)]
visited = [False] * n
ans =[]

solve(0,n,temp,visited,A,ans)
print(ans)
