"""Bellman-Ford shortest path supporting negative edge weights."""
from typing import List, Tuple

def bellman_ford(num_nodes: int, edges: List[Tuple[int, int, int]], start: int):
    dist = [float('inf')] * num_nodes
    dist[start] = 0
    for _ in range(num_nodes - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Negative weight cycle detected")
    return dist
