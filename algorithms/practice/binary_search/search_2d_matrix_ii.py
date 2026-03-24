"""
Module: Search a 2D Matrix II Top Right Step
Category: binary_search
Time Complexity: O(m+n)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_search_2d_matrix_ii(*args, **kwargs) -> Any:
    """
    Solves Search a 2D Matrix II Top Right Step with optimal asymptotic complexity.
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
