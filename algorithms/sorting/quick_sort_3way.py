"""3-way partitioning QuickSort optimized for repeated keys."""
from typing import List

def quick_sort_3way(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None: high = len(arr) - 1
    if low >= high: return arr
    lt = low; gt = high; v = arr[low]; i = low + 1
    while i <= gt:
        if arr[i] < v:
            arr[lt], arr[i] = arr[i], arr[lt]; lt += 1; i += 1
        elif arr[i] > v:
            arr[i], arr[gt] = arr[gt], arr[i]; gt -= 1
        else: i += 1
    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)
    return arr
