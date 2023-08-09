class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def find_middle(A):
    slow = A
    fast = A
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def reverse(A):
    prv = None
    curr = A
    while curr:
        temp = curr.next
        curr.next = prv
        prv = curr
        curr = temp
    return prv


def solve(A):
    head = A
    middle = find_middle(head)
    h2 =middle.next
    middle.next = None
    t1 = A
    t2 = reverse(h2)
    while t1 and t2:
        if t1.val != t2.val:
            return 0
        t1 = t1.next
        t2 = t2.next
    return 1


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
print(solve(head))


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
print(solve(head))
