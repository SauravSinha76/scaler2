

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(A, B):
    temp = A
    count = 0
    while temp:
        temp = temp.next
        count += 1

    if B >= count:
        A = A.next
        return A

    idx = count - B
    temp = A
    while idx > 1:
        temp = temp.next
        idx -= 1
    temp.next = temp.next.next
    return A


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
new_head = solve(head,2)
while new_head:
    print(new_head.val)
    new_head = new_head.next


