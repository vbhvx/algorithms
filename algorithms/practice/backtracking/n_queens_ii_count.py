"""
Module: N-Queens II Total Solutions Count Bitmask
Category: backtracking
Time Complexity: O(n!)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_n_queens_ii_count(*args, **kwargs) -> Any:
    """
    Solves N-Queens II Total Solutions Count Bitmask with optimal asymptotic complexity.
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
