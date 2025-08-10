"""Topological sort of Directed Acyclic Graph (DAG) using in-degrees."""
from collections import deque
from typing import Dict, List

def topological_sort_kahn(num_nodes: int, edges: List[tuple]) -> List[int]:
    adj = {i: [] for i in range(num_nodes)}
    in_degree = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v); in_degree[v] += 1
    q = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0: q.append(v)
    if len(order) != num_nodes: raise ValueError("Graph has cycles")
    return order
