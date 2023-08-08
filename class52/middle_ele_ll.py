def solve(A):
    slow = A
    fast = A

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    return slow.val
