"""
Empirical benchmark for Minimum Number of Refueling Stops MaxHeap
"""
import time
from algorithms.practice.heaps_and_priority.min_refuel_stops import solve_min_refuel_stops

def benchmark_min_refuel_stops():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_refuel_stops([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_refuel_stops()
    print(f"Minimum Number of Refueling Stops MaxHeap 100 iterations took {t*1000:.3f}ms")
