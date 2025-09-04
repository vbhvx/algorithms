"""Kadane's algorithm finding maximum subarray sum in O(n)."""
from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    cur_sum = max_sum = nums[0]
    for x in nums[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum
