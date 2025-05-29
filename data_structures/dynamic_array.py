"""Dynamic array with O(1) amortized append and automatic resizing."""

class DynamicArray:
    def __init__(self, initial_capacity: int = 4):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * initial_capacity

    def append(self, val):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.size] = val
        self.size += 1

    def _resize(self, new_cap: int):
        new_data = [None] * new_cap
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_cap

    def get(self, idx: int):
        if idx < 0 or idx >= self.size: raise IndexError("Index out of range")
        return self.data[idx]

    def pop(self):
        if self.size == 0: raise IndexError("Pop from empty array")
        val = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return val
