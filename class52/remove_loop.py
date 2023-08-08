def solve(A):
    slow = A
    fast = A
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow = A
    pev = fast

    while slow != fast:
        pev = fast
        slow = slow.next
        fast = fast.next

    pev.next = None

    return A
