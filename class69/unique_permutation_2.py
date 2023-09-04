def uni_per(idx,n,temp,freq,ans):

    if idx == n:
        ans.append(list(temp))
        return

    for i in range(len(freq)):
        if freq[i] >0:
            freq[i] -= 1
            temp[idx] = i
            uni_per(idx +1, n, temp,freq,ans)
            freq[i] += 1

def solve(A):
    n = len(A)
    freq =[0] * 11
    for a in A:
        freq[a] += 1

    ans =[]
    temp =[0] * n
    uni_per(0,n,temp,freq,ans)
    return ans

A =[1,1,2]
print(solve(A))