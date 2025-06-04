"""Doubly linked list with sentinel nodes."""

class DNode:
    def __init__(self, val=None):
        self.val = val; self.prev = None; self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = DNode(); self.tail = DNode()
        self.head.next = self.tail; self.tail.prev = self.head
        self.size = 0

    def append(self, val):
        node = DNode(val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove(self, node: DNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
