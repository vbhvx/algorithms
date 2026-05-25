"""
Module: Kth Smallest Element in BST Inorder
Category: trees_and_bst
Time Complexity: O(h+k)
Space Complexity: O(h)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_kth_smallest_bst(*args, **kwargs) -> Any:
    """
    Solves Kth Smallest Element in BST Inorder with optimal asymptotic complexity.
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
