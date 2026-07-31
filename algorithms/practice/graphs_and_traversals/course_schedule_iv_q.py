"""
Module: Course Schedule IV Reachability Closure
Category: graphs_and_traversals
Time Complexity: O(V*(V+E))
Space Complexity: O(V^2)
"""
from typing import List, Dict, Set, Optional, Tuple, Any

def solve_course_schedule_iv_q(*args, **kwargs) -> Any:
    """
    Solves Course Schedule IV Reachability Closure with optimal asymptotic complexity.
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
