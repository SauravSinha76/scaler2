from class25.linked_list import Node


def solve(A,B):
    temp = A
    idx = 0
    while B > idx:
        temp = temp.next
        idx += 1
    return temp.val

head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(1)
print(solve(head,1))
