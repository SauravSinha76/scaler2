class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



def partion(A,B):
    d1 = Node(-1)
    d2 = Node(-1)

    t1 = d1
    t2 = d2

    temp = A
    while temp:
        if temp.val < B:
            t1.next = temp
            t1 = t1.next
        else:
            t2.next = temp
            t2 = t2.next
        temp = temp.next
    t2.next = None
    t1.next = d2.next

    return d1.next

head = Node(1)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(2)
new_head = partion(head,3)
while new_head:
    print(new_head.val)
    new_head = new_head.next

