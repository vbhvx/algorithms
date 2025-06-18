"""Sliding window maximum in O(n) using a double-ended queue."""
from collections import deque
from typing import List

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []
    for i, n in enumerate(nums):
        while q and nums[q[-1]] < n:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
