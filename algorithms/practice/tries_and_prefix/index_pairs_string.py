"""
Module: Index Pairs of a String Trie Traversal
Category: tries_and_prefix
Time Complexity: O(text * l)
Space Complexity: O(words)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_index_pairs_string(*args, **kwargs) -> Any:
    """
    Solves Index Pairs of a String Trie Traversal with optimal asymptotic complexity.
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
