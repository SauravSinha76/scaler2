def sub(idx,n,A,temp,ans):
    if idx == n:
        ans.append(list(temp))
        return

    sub(idx + 1, n, A, temp, ans)


    temp.append(A[idx])
    sub(idx + 1, n , A, temp, ans)
    temp.pop()



def solve(A):
    n = len(A)
    ans =[]
    sub(0,n,A,[],ans)
    return ans

A = 'saurav'
for a in solve(A):
    print(a)

