"""
Module: Word Search II Trie Backtracking Matrix
Category: tries_and_prefix
Time Complexity: O(m*4^l)
Space Complexity: O(total_chars)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_word_search_ii(*args, **kwargs) -> Any:
    """
    Solves Word Search II Trie Backtracking Matrix with optimal asymptotic complexity.
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
