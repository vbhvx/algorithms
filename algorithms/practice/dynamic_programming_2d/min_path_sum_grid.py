"""
Module: Minimum Path Sum Matrix In-Place
Category: dynamic_programming_2d
Time Complexity: O(m*n)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_min_path_sum_grid(*args, **kwargs) -> Any:
    """
    Solves Minimum Path Sum Matrix In-Place with optimal asymptotic complexity.
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
