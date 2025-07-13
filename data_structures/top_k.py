"""Find Top-K frequent elements in O(n log k) using min-heap."""
from collections import Counter
import heapq
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    return [item[0] for item in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]
