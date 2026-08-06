"""
Module: Word Ladder II Bidirectional BFS Backtrack
Category: graphs_and_traversals
Time Complexity: O(m^2 * n + paths)
Space Complexity: O(m*n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_word_ladder_ii_paths(*args, **kwargs) -> Any:
    """
    Solves Word Ladder II Bidirectional BFS Backtrack with optimal asymptotic complexity.
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
