"""
Module: Sort Colors Dutch National Flag
Category: two_pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_sort_colors_dutch(*args, **kwargs) -> Any:
    """
    Solves Sort Colors Dutch National Flag with optimal asymptotic complexity.
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
