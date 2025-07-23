"""Segment Tree for O(log n) range minimum queries and point updates."""
from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0: self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]; return
        mid = (start + end) // 2
        self._build(arr, 2 * node + 1, start, mid)
        self._build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, l, r):
        if r < start or end < l: return float('inf')
        if l <= start and end <= r: return self.tree[node]
        mid = (start + end) // 2
        return min(self.query(2 * node + 1, start, mid, l, r),
                   self.query(2 * node + 2, mid + 1, end, l, r))
