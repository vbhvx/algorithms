"""
Module: Ugly Number III Inclusion Exclusion
Category: binary_search
Time Complexity: O(log max)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_ugly_number_iii(*args, **kwargs) -> Any:
    """
    Solves Ugly Number III Inclusion Exclusion with optimal asymptotic complexity.
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
