"""Prim's MST algorithm using min-heap priority queue."""
import heapq
from typing import List, Tuple

def prim_mst(num_nodes: int, edges: List[Tuple[int, int, int]]) -> int:
    adj = {i: [] for i in range(num_nodes)}
    for u, v, w in edges:
        adj[u].append((v, w)); adj[v].append((u, w))
    visited = set([0]); pq = []
    for v, w in adj[0]: heapq.heappush(pq, (w, 0, v))
    total_weight = 0
    while pq and len(visited) < num_nodes:
        w, u, v = heapq.heappop(pq)
        if v in visited: continue
        visited.add(v); total_weight += w
        for nxt, nw in adj[v]:
            if nxt not in visited: heapq.heappush(pq, (nw, v, nxt))
    return total_weight
