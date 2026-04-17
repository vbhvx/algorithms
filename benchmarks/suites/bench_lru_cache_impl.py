"""
Empirical benchmark for LRU Cache Doubly Linked List Hash Map
"""
import time
from algorithms.practice.linked_lists.lru_cache_impl import solve_lru_cache_impl

def benchmark_lru_cache_impl():
    start = time.perf_counter()
    for _ in range(100):
        solve_lru_cache_impl([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_lru_cache_impl()
    print(f"LRU Cache Doubly Linked List Hash Map 100 iterations took {t*1000:.3f}ms")
