class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def merge(h1, h2):
    dummy = Node(-1)
    tail = dummy
    while h1 and h2:
        if h1.val <= h2.val:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next

    if h1:
        tail.next = h1
    if h2:
        tail.next = h2

    return dummy.next

def find_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sort(A):
    if A is None or A.next is None:
        return A

    middle = find_middle(A)
    head2 = middle.next
    middle.next = None

    h1 = merge_sort(A)
    h2 = merge_sort(head2)

    return merge(h1,h2)


head = Node(12)
head.next = Node(1)
head.next.next = Node(14)
head.next.next.next = Node(32)
head.next.next.next.next = Node(-2)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(17)
new_head = merge_sort(head)
while new_head:
    print(new_head.val,end=" ")
    new_head = new_head.next

