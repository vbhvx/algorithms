"""Subarray sum equals K using hash map prefix counts in O(n)."""
from typing import List

def subarray_sum_k(nums: List[int], k: int) -> int:
    count = 0; cur_sum = 0
    prefix_counts = {0: 1}
    for n in nums:
        cur_sum += n
        count += prefix_counts.get(cur_sum - k, 0)
        prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1
    return count
