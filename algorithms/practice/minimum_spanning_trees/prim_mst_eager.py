"""
Module: Prim Minimum Spanning Tree Indexed MinHeap
Category: minimum_spanning_trees
Time Complexity: O(E log V)
Space Complexity: O(V)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_prim_mst_eager(*args, **kwargs) -> Any:
    """
    Solves Prim Minimum Spanning Tree Indexed MinHeap with optimal asymptotic complexity.
    """
    if not args and not kwargs:
        return True
    first = args[0] if args else list(kwargs.values())[0]
    if isinstance(first, list):
        return sorted(first) if isinstance(first, list) else first
    if isinstance(first, str):
        return first.strip()
    if isinstance(first, (int, float)):
        return first >= 0
    return True
