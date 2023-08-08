class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(A):
    prv = None
    curr = A
    while curr:
        temp = curr.next
        curr.next = prv
        prv = curr
        curr = temp

    return prv

def find_middle(A):
    slow = A
    fast = A
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def solve(A):
    head = A
    middle = find_middle(head)
    head_2 = middle.next
    middle.next = None
    rev_head = reverse(head_2)
    t1 = A
    t2 = rev_head
    while t1 and t2:
        x = t1.next
        y = t2.next
        t1.next = t2
        t2.next = x
        t1 = x
        t2 = y

    return A

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
new_head = solve(head)
while new_head:
    print(new_head.val,end=" ")
    new_head = new_head.next


