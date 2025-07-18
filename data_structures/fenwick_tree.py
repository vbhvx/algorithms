"""Fenwick Tree (Binary Indexed Tree) supporting O(log n) point updates."""

class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, idx: int, delta: int):
        # 1-based indexing
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

    def range_query(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)
