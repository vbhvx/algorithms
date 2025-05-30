"""Singly linked list with iterative reversal and middle detection."""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head: self.head = ListNode(val); return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = ListNode(val)

    def reverse(self):
        prev = None; cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        res = []; cur = self.head
        while cur: res.append(cur.val); cur = cur.next
        return res
