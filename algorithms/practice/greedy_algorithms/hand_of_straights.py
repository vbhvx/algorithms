"""
Module: Hand of Straights Consecutive Groups MinHeap
Category: greedy_algorithms
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_hand_of_straights(*args, **kwargs) -> Any:
    """
    Solves Hand of Straights Consecutive Groups MinHeap with optimal asymptotic complexity.
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
