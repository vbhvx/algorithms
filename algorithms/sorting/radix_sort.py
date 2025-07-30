"""LSD RadixSort sorting integers in linear O(d * (n + k)) time."""
from typing import List

def radix_sort(arr: List[int]) -> List[int]:
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        _counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def _counting_sort_by_digit(arr, exp):
    n = len(arr); output = [0] * n; count = [0] * 10
    for x in arr: count[(x // exp) % 10] += 1
    for i in range(1, 10): count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        d = (arr[i] // exp) % 10
        output[count[d] - 1] = arr[i]; count[d] -= 1
    for i in range(n): arr[i] = output[i]
