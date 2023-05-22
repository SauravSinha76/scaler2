from class25.linked_list import Node


def delete(A,B):
    if B ==0:
        A = A.next
    else:
        temp = A
        idx = 1
        while B > idx:
            temp = temp.next
            idx += 1

        temp.next = temp.next.next

    return A

head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(1)
ll = delete(head,3)
while ll:
    print(ll.val)
    ll = ll.next

