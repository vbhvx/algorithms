"""
Empirical benchmark for Find K-th Smallest Pair Distance
"""
import time
from algorithms.practice.binary_search.kth_smallest_pair_dist import solve_kth_smallest_pair_dist

def benchmark_kth_smallest_pair_dist():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_smallest_pair_dist([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_smallest_pair_dist()
    print(f"Find K-th Smallest Pair Distance 100 iterations took {t*1000:.3f}ms")
