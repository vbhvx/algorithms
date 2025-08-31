"""Longest Increasing Subsequence using patience sorting / bisect."""
from bisect import bisect_left
from typing import List

def length_of_lis(nums: List[int]) -> int:
    sub = []
    for x in nums:
        idx = bisect_left(sub, x)
        if idx == len(sub): sub.append(x)
        else: sub[idx] = x
    return len(sub)
