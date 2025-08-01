"""Lower bound and Upper bound bisect operations."""
from typing import List

def lower_bound(arr: List[int], target: int) -> int:
    low = 0; high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target: low = mid + 1
        else: high = mid
    return low

def upper_bound(arr: List[int], target: int) -> int:
    low = 0; high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target: low = mid + 1
        else: high = mid
    return low
