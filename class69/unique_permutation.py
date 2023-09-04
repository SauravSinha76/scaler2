def perm(idx,freq,temp,n,A,ans):
    if idx == n:
        ans.append(list(temp))
        return

    for i in range(len(freq)):
        if freq[i] > 0:
            freq[i] -= 1
            temp[idx] = chr(i + ord('a'))
            perm(idx + 1, freq,temp,n,A,ans)
            freq[i] += 1

def solve(A):
    freq=[0] * 26
    n = len(A)
    for a in A:
        freq[ord(a) - ord('a')] += 1
    temp = [''] *n
    ans =[]
    perm(0,freq,temp,n,A,ans)
    return ans

from collections import Counter

s = 'aac'
print(solve(s))

