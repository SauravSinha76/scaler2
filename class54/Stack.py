class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(-1)
        self.size = -1

    def push(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def top(self):
        return self.head.next.val

    def pop(self):
        if self.size == -1:
            print("Stack is empty")
        else:
            temp = self.head.next.val
            self.head.next = self.head.next.next
            self.size -= 1
            return temp

