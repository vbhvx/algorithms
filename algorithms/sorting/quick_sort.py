"""In-place QuickSort algorithm with Lomuto partition scheme."""
from typing import List

def quick_sort(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None: high = len(arr) - 1
    if low < high:
        pi = _partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def _partition(arr, low, high):
    pivot = arr[high]; i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
