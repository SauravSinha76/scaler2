class RandomNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None

def solve(head):
    temp = head
    hm ={}
    new_head = RandomNode(temp.val)
    hm[temp] = new_head
    while temp.next:
        new_head.next = RandomNode(temp.next.val)
        new_head = new_head.next
        temp = temp.next
        hm[temp] = new_head

    temp = head
    while temp:
        hm[temp].random = hm.get(temp.random,None)
        temp = temp.next
    return hm[head]

def solve_2(A):
    temp = A

    while temp:
        nn = RandomNode(temp.val)
        nn.next = temp.next
        temp.next = nn
        temp = temp.next.next

    temp = A

    while temp:
        temp.next.random = temp.random.next
        temp = temp.next.next

    head = A
    head2 = A.next
    temp1 = head
    temp2 = head2

    while temp2.next:
        temp1.next = temp1.next.next
        temp2.next = temp2.next.next

        temp1 = temp1.next
        temp2 = temp2.next

    temp1.next = None
    return head2






head = RandomNode(1)
two = RandomNode(2)
head.next = two
three = RandomNode(3)
two.next = three
head.random = three
# three.random = head
two.random = head
new_head = solve(head)
while new_head:
    print(new_head.val,end=" ")
    new_head = new_head.next


head = RandomNode(1)
two = RandomNode(2)
head.next = two
three = RandomNode(3)
two.next = three
head.random = three
three.random = head
two.random = head
new_head = solve_2(head)
while new_head:
    print(new_head.val,end=" ")
    new_head = new_head.next