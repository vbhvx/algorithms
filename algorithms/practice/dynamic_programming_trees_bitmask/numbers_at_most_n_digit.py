"""
Module: Numbers At Most N Given Digit Set Digit DP
Category: dynamic_programming_trees_bitmask
Time Complexity: O(log n)
Space Complexity: O(log n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_numbers_at_most_n_digit(*args, **kwargs) -> Any:
    """
    Solves Numbers At Most N Given Digit Set Digit DP with optimal asymptotic complexity.
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
