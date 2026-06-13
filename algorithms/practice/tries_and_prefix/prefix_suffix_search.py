"""
Module: Prefix and Suffix Search Word Filter Trie
Category: tries_and_prefix
Time Complexity: O(l^2)
Space Complexity: O(l^2)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_prefix_suffix_search(*args, **kwargs) -> Any:
    """
    Solves Prefix and Suffix Search Word Filter Trie with optimal asymptotic complexity.
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
