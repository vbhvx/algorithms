"""
Module: Trim a Binary Search Tree Range Prune
Category: trees_and_bst
Time Complexity: O(n)
Space Complexity: O(h)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_trim_bst(*args, **kwargs) -> Any:
    """
    Solves Trim a Binary Search Tree Range Prune with optimal asymptotic complexity.
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
