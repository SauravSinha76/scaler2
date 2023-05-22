from class25.linked_list import Node


def solve(node):
    if node == None:
        return
    solve(node.next)
    print(node.val)


def reverse(head):
    solve(head)



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
reverse(head)