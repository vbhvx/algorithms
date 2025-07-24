"""Stable O(n log n) MergeSort implementation."""
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []; i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: res.append(left[i]); i += 1
        else: res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res
