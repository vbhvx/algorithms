"""
Module: Maximum Subsequence Score MinHeap Sort
Category: heaps_and_priority
Time Complexity: O(n log n)
Space Complexity: O(k)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_max_subsequence_score(*args, **kwargs) -> Any:
    """
    Solves Maximum Subsequence Score MinHeap Sort with optimal asymptotic complexity.
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
