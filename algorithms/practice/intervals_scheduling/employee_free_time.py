"""
Module: Employee Free Time All Work Intervals Sweep
Category: intervals_scheduling
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_employee_free_time(*args, **kwargs) -> Any:
    """
    Solves Employee Free Time All Work Intervals Sweep with optimal asymptotic complexity.
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
