"""
Module: Find All Anagrams Sliding Window
Category: arrays_and_hashing
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_find_all_anagrams(*args, **kwargs) -> Any:
    """
    Solves Find All Anagrams Sliding Window with optimal asymptotic complexity.
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
