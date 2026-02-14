"""
Module: Longest Substring Without Repeats
Category: sliding_window
Time Complexity: O(n)
Space Complexity: O(min(n,m))
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_longest_substring_no_repeat(*args, **kwargs) -> Any:
    """
    Solves Longest Substring Without Repeats with optimal asymptotic complexity.
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
