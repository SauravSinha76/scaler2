from class25.linked_list import Node


def solve(A):
    prv = A
    temp = A.next
    while temp:
        if prv.val > temp.val:
            return 0
        prv = temp
        temp = temp.next
    return 1

head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(1)
print(solve(head))