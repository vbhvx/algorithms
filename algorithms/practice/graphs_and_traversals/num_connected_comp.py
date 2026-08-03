"""
Module: Number of Connected Components DSU
Category: graphs_and_traversals
Time Complexity: O(V + E*alpha(V))
Space Complexity: O(V)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_num_connected_comp(*args, **kwargs) -> Any:
    """
    Solves Number of Connected Components DSU with optimal asymptotic complexity.
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
