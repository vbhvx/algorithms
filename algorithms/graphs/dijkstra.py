"""Dijkstra's shortest path algorithm for non-negative weights."""
import heapq
from typing import Dict, List, Tuple

def dijkstra(num_nodes: int, edges: List[Tuple[int, int, int]], start: int) -> Dict[int, int]:
    adj = {i: [] for i in range(num_nodes)}
    for u, v, w in edges: adj[u].append((v, w))
    dist = {i: float('inf') for i in range(num_nodes)}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
