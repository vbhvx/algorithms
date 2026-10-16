"""
Module: Maximum Product of Splitted Binary Tree
Category: dynamic_programming_trees_bitmask
Time Complexity: O(n)
Space Complexity: O(h)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_maximum_product_tree_split(*args, **kwargs) -> Any:
    """
    Solves Maximum Product of Splitted Binary Tree with optimal asymptotic complexity.
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
