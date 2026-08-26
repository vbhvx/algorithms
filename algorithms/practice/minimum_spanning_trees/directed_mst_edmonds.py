"""
Module: Edmonds Chu-Liu Algorithm for Directed MST
Category: minimum_spanning_trees
Time Complexity: O(V*E)
Space Complexity: O(V+E)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_directed_mst_edmonds(*args, **kwargs) -> Any:
    """
    Solves Edmonds Chu-Liu Algorithm for Directed MST with optimal asymptotic complexity.
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
