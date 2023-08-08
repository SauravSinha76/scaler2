import http.client


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def solve(A,B):
    t1 = A
    t2 = B
    carry = 0
    C = Node(-1)
    temp = C
    while t1 and t2:
        add = t1.val + t2.val + carry

        temp.next = Node(add % 10)
        carry = add // 10
        t1 = t1.next
        t2 = t2.next
        temp = temp.next

    while t1:
        add = t1.val + carry
        temp.next = Node(add % 10)
        carry = add // 10
        t1 = t1.next
        temp = temp.next

    while t2:
        add = t2.val + carry

        temp.next = Node(add % 10)
        carry = add // 10

        t2 = t2.next
        temp = temp.next

    while carry > 0:
        temp.next = Node(carry % 10)
        carry //= 10

    return C.next


A = Node(9)
A.next = Node(9)
A.next.next = Node(9)

B = Node(1)
# B.next = Node(6)
# B.next.next = Node(4)
new_node = solve(A,B)
while new_node:
    print(new_node.val, end=" ")
    new_node = new_node.next
