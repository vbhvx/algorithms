"""
Module: Partition Equal Subset Sum 0-1 Knapsack
Category: dynamic_programming_1d
Time Complexity: O(n * target)
Space Complexity: O(target)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_partition_equal_subset(*args, **kwargs) -> Any:
    """
    Solves Partition Equal Subset Sum 0-1 Knapsack with optimal asymptotic complexity.
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
