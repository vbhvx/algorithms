"""Kruskal's MST algorithm using Disjoint Set Union."""
from data_structures.union_find import UnionFind
from typing import List, Tuple

def kruskal_mst(num_nodes: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
    sorted_edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(num_nodes)
    mst = []; total_weight = 0
    for u, v, w in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == num_nodes - 1: break
    return total_weight, mst
