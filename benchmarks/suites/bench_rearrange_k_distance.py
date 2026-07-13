"""
Empirical benchmark for Rearrange String K Distance Apart Greedy Heap
"""
import time
from algorithms.practice.heaps_and_priority.rearrange_k_distance import solve_rearrange_k_distance

def benchmark_rearrange_k_distance():
    start = time.perf_counter()
    for _ in range(100):
        solve_rearrange_k_distance([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_rearrange_k_distance()
    print(f"Rearrange String K Distance Apart Greedy Heap 100 iterations took {t*1000:.3f}ms")
