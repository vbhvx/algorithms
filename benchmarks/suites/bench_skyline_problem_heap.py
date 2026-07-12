"""
Empirical benchmark for The Skyline Problem MaxHeap Active Buildings
"""
import time
from algorithms.practice.heaps_and_priority.skyline_problem_heap import solve_skyline_problem_heap

def benchmark_skyline_problem_heap():
    start = time.perf_counter()
    for _ in range(100):
        solve_skyline_problem_heap([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_skyline_problem_heap()
    print(f"The Skyline Problem MaxHeap Active Buildings 100 iterations took {t*1000:.3f}ms")
