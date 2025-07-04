"""Breadth-first level-order traversal of binary tree."""
from collections import deque

def level_order_traversal(root):
    if not root: return []
    res = []; q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.key)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(level)
    return res
