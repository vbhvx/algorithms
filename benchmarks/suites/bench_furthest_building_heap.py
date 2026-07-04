"""
Empirical benchmark for Furthest Building You Can Reach MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.furthest_building_heap import solve_furthest_building_heap

def benchmark_furthest_building_heap():
    start = time.perf_counter()
    for _ in range(100):
        solve_furthest_building_heap([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_furthest_building_heap()
    print(f"Furthest Building You Can Reach MinHeap 100 iterations took {t*1000:.3f}ms")
