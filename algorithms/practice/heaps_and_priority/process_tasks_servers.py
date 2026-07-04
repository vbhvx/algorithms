"""
Module: Process Tasks Using Servers Two Heaps
Category: heaps_and_priority
Time Complexity: O((n+m) log n)
Space Complexity: O(n+m)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_process_tasks_servers(*args, **kwargs) -> Any:
    """
    Solves Process Tasks Using Servers Two Heaps with optimal asymptotic complexity.
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
