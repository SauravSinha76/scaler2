def solve(A):
    n = len(A)
    ans =[]
    for i in range(n):
        for j in range(i+1, n):
            ans.append(A[i:j])
    return ans

def solve_rec(i,n,A,temp):
    if i == n:
        print(temp)
        return

    solve_rec(i + 1, n, A, temp)

    temp.append(A[i])
    solve_rec(i+1,n,A,temp)
    temp.pop()


def permu(idx,n,A,temp,visited):

    if idx == n:
        print(temp)
        return

    for i in range(len(A)):
        if visited[i] == False:
            visited[i] = True
            temp.append(A[i])
            permu(idx + 1, n,A,temp,visited)
            temp.pop()
            visited[i] = False


A = "abc"
# ans  = solve(A)
# print(ans)
# print(len(ans))
# solve_rec(0,len(A),A,[])
temp =[]* len(A)
visited =[False] * len(A)
permu(0,len(A),A,[],visited)