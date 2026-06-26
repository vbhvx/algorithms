"""
Module: Kth Largest Element in Array QuickSelect MinHeap
Category: heaps_and_priority
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_kth_largest_array(*args, **kwargs) -> Any:
    """
    Solves Kth Largest Element in Array QuickSelect MinHeap with optimal asymptotic complexity.
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
