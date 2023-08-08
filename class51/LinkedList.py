


def printLL(head):
    temp = head
    while temp.next:
        print(temp.val, end=" ")
        temp = temp.next
    print(temp.val)


class LL:
    def __init__(self):
        self.length = 0
        self.head = None

    def printLL(self):
        temp = self.head
        while temp.next:
            print(temp.val, end=" ")
            temp = temp.next
        print(temp.val)

    def insert(self, position, value):
        if position > self.length + 1:
            return

        newNode = Node(value)

        if position == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            c = 1
            while c < position - 1:
                temp = temp.next
                c += 1
            newNode.next = temp.next
            temp.next = newNode
        self.length += 1

    def delete(self, postion):
        if postion > self.length:
            return

        temp = self.head
        if postion == 1:
            self.head = self.head.next
        else:
            c = postion
            while c < postion - 1:
                temp = temp.next
                c += 1
            temp.next = temp.next.next
            self.length -= 1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
ll = LL()
ll.insert(1,1)
ll.insert(2,2)
ll.insert(3,3)
ll.insert(4,4)
ll.printLL()
ll.delete(2)
ll.printLL()
