"""
Empirical benchmark for K Closest Points to Origin MaxHeap
"""
import time
from algorithms.practice.heaps_and_priority.k_closest_points import solve_k_closest_points

def benchmark_k_closest_points():
    start = time.perf_counter()
    for _ in range(100):
        solve_k_closest_points([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_k_closest_points()
    print(f"K Closest Points to Origin MaxHeap 100 iterations took {t*1000:.3f}ms")
