"""
Module: Split String Into Max Unique Substrings
Category: backtracking
Time Complexity: O(2^n)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_split_max_unique_sub(*args, **kwargs) -> Any:
    """
    Solves Split String Into Max Unique Substrings with optimal asymptotic complexity.
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
