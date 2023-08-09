class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.down = None


def merge(A,B):
    dummy = Node(-1)

    tail = dummy
    A.next = B.next
    while A and B:
        if A.val <= B.val:
            tail.down = A
            A = A.down
        else:
            tail.down = B
            B = B.down
        tail = tail.down

    if A:
        tail.down = A
    if B:
        tail.down = B
    return dummy.down

def faltten(root):
    temp = root
    while temp.next:
        temp = merge(temp,temp.next)
    return root

head = Node(3)
head.next = Node(4)
head.next.next = Node(20)
head.next.next.next = Node(20)
head.next.next.next.next = Node(30)

head.down = Node(7)
head.down.down = Node(8)

head.next.down = Node(11)

head.next.next.down = Node(22)

head.next.next.next.down = Node(20)
head.next.next.next.down.down = Node(20)
head.next.next.next.down.down.down = Node(28)
head.next.next.next.down.down.down.down = Node(39)

head.next.next.next.next.down = Node(31)
head.next.next.next.next.down.down = Node(39)

new_head = faltten(head)
while new_head:
    print(new_head.val)
    new_head = new_head.down
