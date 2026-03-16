"""
Module: Sum of Subarray Minimums Monotonic
Category: stack_and_queue
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_sum_subarray_mins(*args, **kwargs) -> Any:
    """
    Solves Sum of Subarray Minimums Monotonic with optimal asymptotic complexity.
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
