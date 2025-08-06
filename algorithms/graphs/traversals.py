"""Standard BFS and DFS graph traversals."""
from collections import deque
from typing import Dict, List

def bfs_traversal(adj: Dict[int, List[int]], start: int) -> List[int]:
    visited = {start}; q = deque([start]); order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v); q.append(v)
    return order

def dfs_traversal(adj: Dict[int, List[int]], start: int) -> List[int]:
    visited = set(); order = []
    def dfs(u):
        visited.add(u); order.append(u)
        for v in adj.get(u, []):
            if v not in visited: dfs(v)
    dfs(start); return order
