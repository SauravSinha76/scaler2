from class25.linked_list import Node


def insert(A,B,C):
    nn = Node(B)
    if C == 0:
        nn.next = A
        A = nn
    temp = A
    idx = 1
    while C > idx and  temp.next:
        idx += 1
        temp = temp.next

    nn.next = temp.next
    temp.next = nn


    return A

head = Node(1)
head.next = Node(2)
B = 3
C = 1

ll = insert(head,B,C)
while ll:
    print(ll.val)
    ll = ll.next
