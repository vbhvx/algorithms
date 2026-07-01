"""
Empirical benchmark for Find K Pairs with Smallest Sums MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.find_k_pairs_smallest import solve_find_k_pairs_smallest

def benchmark_find_k_pairs_smallest():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_k_pairs_smallest([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_k_pairs_smallest()
    print(f"Find K Pairs with Smallest Sums MinHeap 100 iterations took {t*1000:.3f}ms")
