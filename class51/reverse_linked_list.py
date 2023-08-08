from class51.LinkedList import Node, printLL


def solve(head):
    pev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = pev
        pev = curr
        curr = temp
    return pev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printLL(head)
new_head = solve(head)
printLL(new_head)