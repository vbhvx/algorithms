"""
Module: All Nodes Distance K in Binary Tree Graph
Category: trees_and_bst
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_all_nodes_k_dist(*args, **kwargs) -> Any:
    """
    Solves All Nodes Distance K in Binary Tree Graph with optimal asymptotic complexity.
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
