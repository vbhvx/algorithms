"""MinHeap implementation from binary array representation."""

class MinHeap:
    def __init__(self): self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap: raise IndexError("Pop from empty heap")
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        if self.heap: self._sift_down(0)
        return val

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            idx = parent; parent = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.heap)
        while 2 * idx + 1 < n:
            child = 2 * idx + 1
            if child + 1 < n and self.heap[child + 1] < self.heap[child]:
                child += 1
            if self.heap[child] < self.heap[idx]:
                self._swap(idx, child); idx = child
            else: break

    def _swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
