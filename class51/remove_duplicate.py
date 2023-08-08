class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(A):
    temp = A
    while temp and temp.next:
        while temp.next and  temp.val == temp.next.val:
            temp.next = temp.next.next
        temp = temp.next
    return A

head = Node(1)
head.next = Node(1)
head.next.next = Node(2)

new_head = solve(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next
