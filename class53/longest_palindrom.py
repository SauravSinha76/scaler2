def count_lengt(h1,h2):
    count =0
    while h1 and h2:
        if h1.val == h2.val:
            count += 1
        else:
            break
        h1 = h1.next
        h2 = h2.next

    return count

def solve(A):
    prv = None
    curr = A
    ans = 0
    while curr:
        temp = curr.next
        curr.next = prv

        ans = max(ans,2 * count_lengt(prv,temp) +1)
        ans = max(ans,2 * count_lengt(curr,temp))

        prv = curr
        curr = temp
    return ans
