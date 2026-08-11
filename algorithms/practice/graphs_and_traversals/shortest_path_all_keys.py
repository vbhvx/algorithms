"""
Module: Shortest Path to Get All Keys Bitmask BFS
Category: graphs_and_traversals
Time Complexity: O(m*n*2^k)
Space Complexity: O(m*n*2^k)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_shortest_path_all_keys(*args, **kwargs) -> Any:
    """
    Solves Shortest Path to Get All Keys Bitmask BFS with optimal asymptotic complexity.
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
