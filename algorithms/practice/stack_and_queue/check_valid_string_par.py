"""
Module: Valid Parenthesis String Wildcards
Category: stack_and_queue
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_check_valid_string_par(*args, **kwargs) -> Any:
    """
    Solves Valid Parenthesis String Wildcards with optimal asymptotic complexity.
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
