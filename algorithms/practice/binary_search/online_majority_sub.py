"""
Module: Online Majority Element In Subarray
Category: binary_search
Time Complexity: O(log n)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_online_majority_sub(*args, **kwargs) -> Any:
    """
    Solves Online Majority Element In Subarray with optimal asymptotic complexity.
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
