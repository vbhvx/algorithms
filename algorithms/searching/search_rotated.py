"""Search in rotated sorted array in O(log n) time."""
from typing import List

def search_rotated(nums: List[int], target: int) -> int:
    low = 0; high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]: high = mid - 1
            else: low = mid + 1
        else:
            if nums[mid] < target <= nums[high]: low = mid + 1
            else: high = mid - 1
    return -1
