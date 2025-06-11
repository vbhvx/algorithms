"""Monotonic stack finding next greater elements in O(n) time."""
from typing import List

def next_greater_elements(arr: List[int]) -> List[int]:
    res = [-1] * len(arr)
    stack = []  # indices
    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] < x:
            idx = stack.pop()
            res[idx] = x
        stack.append(i)
    return res
