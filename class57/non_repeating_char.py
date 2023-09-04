from collections import deque


def solve(A):
    queue = deque()

    hm={}
    ans =''
    for a in A:
        hm[a] = hm.get(a,0) + 1
        queue.append(a)
        while queue and hm[queue[0]] >= 2:
            queue.popleft()

        if queue:
            ans += queue[0]
        else:
            ans += '#'
    return ans

A = "abadbc"
A = "abcabc"
print(solve(A))
