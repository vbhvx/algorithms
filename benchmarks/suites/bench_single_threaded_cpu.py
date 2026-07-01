"""
Empirical benchmark for Single-Threaded CPU Order Priority Queue
"""
import time
from algorithms.practice.heaps_and_priority.single_threaded_cpu import solve_single_threaded_cpu

def benchmark_single_threaded_cpu():
    start = time.perf_counter()
    for _ in range(100):
        solve_single_threaded_cpu([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_single_threaded_cpu()
    print(f"Single-Threaded CPU Order Priority Queue 100 iterations took {t*1000:.3f}ms")
