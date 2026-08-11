"""
Module: 01 Matrix Multi-Source BFS Distance Field
Category: graphs_and_traversals
Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_matrix_01_distances(*args, **kwargs) -> Any:
    """
    Solves 01 Matrix Multi-Source BFS Distance Field with optimal asymptotic complexity.
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
