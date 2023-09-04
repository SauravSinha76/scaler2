def sub_set(idx,n,A,temp,ans):
    if idx == n:
        ans.append(list(temp))
        return



    temp.append(A[idx])
    sub_set(idx+1,n,A,temp,ans)
    temp.pop()

    sub_set(idx +1, n, A,temp,ans)

def solve(A):
    n = len(A)
    A.sort()
    ans= []
    temp =[]
    sub_set(0,n,A,temp,ans)
    return ans

A =[1,2,3]
for a in solve(A):
    print(a)

