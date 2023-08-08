class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def solve(A):
    dummy = ListNode(-1)

    tail = dummy

    B = dummy.next
    for a in A:
        C = a
        while B and C:
            if B.val < C.val:
                tail.next = B
                B = B.next
            else:
                tail.next = C
                C = C.next
            tail = tail.next

        if not B:
            tail.next = C
        if not C:
            tail.next = B

        B = dummy.next
        tail = dummy

    return dummy.next





A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(5)
A.next.next.next = ListNode(15)

B = ListNode(3)
B.next = ListNode(4)
B.next.next = ListNode(6)
B.next.next.next = ListNode(7)
B.next.next.next.next = ListNode(8)



def solve1(A,B):

    dummy = ListNode(-1)

    tail = dummy

    while A and B:
        if A.val < B.val:
            tail.next = A
            A = A.next
        else:
            tail.next = B
            B = B.next

        tail = tail.next

    if not A:
        tail.next = B

    if not B:
        tail.next = A

    return dummy.next


print(solve1(A,B))
print("solve")