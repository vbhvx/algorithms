"""Stack supporting push, pop, top, and get_min in O(1) time."""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> int:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def get_min(self) -> int:
        return self.min_stack[-1]
