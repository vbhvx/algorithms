"""
Empirical benchmark for LFU Cache Frequency Buckets Doubly Linked
"""
import time
from algorithms.practice.linked_lists.lfu_cache_impl import solve_lfu_cache_impl

def benchmark_lfu_cache_impl():
    start = time.perf_counter()
    for _ in range(100):
        solve_lfu_cache_impl([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_lfu_cache_impl()
    print(f"LFU Cache Frequency Buckets Doubly Linked 100 iterations took {t*1000:.3f}ms")
