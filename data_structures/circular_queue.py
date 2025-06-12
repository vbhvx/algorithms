"""Circular queue implementation with array and head/tail pointers."""

class CircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = 0
        self.count = 0

    def enqueue(self, val) -> bool:
        if self.count == self.k: return False
        tail = (self.head + self.count) % self.k
        self.queue[tail] = val
        self.count += 1
        return True

    def dequeue(self) -> bool:
        if self.count == 0: return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def front(self):
        return self.queue[self.head] if self.count > 0 else -1
