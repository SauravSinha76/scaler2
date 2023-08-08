class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def solve(A,B):
    t1 = A
    t2 = B

    dummy = Node(-1)
    tail = dummy
    while t1 and t2:
        if t1.val <= t2.val:
            tail.next = t1
            t1 = t1.next
        else:
            tail.next = t2
            t2 = t2.next
        tail = tail.next

    if t1:
        tail.next = t1

    if t2:
        tail.next = t2

    return dummy.next

head1 = Node(5)
head1.next = Node(11)
head1.next.next = Node(25)

head2 = Node(1)
head2.next = Node(18)
head2.next.next = Node(35)

new_head = solve(head1,head2)
while new_head:
    print(new_head.val,end=" ")
    new_head = new_head.next