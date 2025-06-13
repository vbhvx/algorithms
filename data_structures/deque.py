"""Double-ended queue supporting O(1) front/back push and pop."""

class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, val): self.items.insert(0, val)
    def push_back(self, val): self.items.append(val)
    def pop_front(self): return self.items.pop(0)
    def pop_back(self): return self.items.pop()
    def size(self): return len(self.items)
