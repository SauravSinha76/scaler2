class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def solve(A,B,C):
    i = 1
    prv = None
    curr = A
    while curr and i < B:
        prv = curr
        curr = curr.next
        i += 1

    start = prv
    end = curr

    while curr and i <= C:
        temp = curr.next

        curr.next = prv
        prv = curr
        curr = temp
        i += 1
    if B == 1:
        A = prv
    else:
        start.next = prv

    end.next = curr

    return A

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

new_head = solve(head,2,4)
while new_head.next:
    print(new_head.val,end=" ")
    new_head = new_head.next

print(new_head.val)

