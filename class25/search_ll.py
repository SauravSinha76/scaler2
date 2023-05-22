from class25.linked_list import Node


def search(A, B):
    temp = A
    while temp:
        if temp.val == B:
            return 1
        temp = temp.next
    return 0

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(search(head,4))

head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(3)
print(search(head,4))