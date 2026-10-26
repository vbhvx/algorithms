"""
Empirical benchmark for Queue Reconstruction by Height Sort Insert
"""
import time
from algorithms.practice.greedy_algorithms.queue_reconstruction import solve_queue_reconstruction

def benchmark_queue_reconstruction():
    start = time.perf_counter()
    for _ in range(100):
        solve_queue_reconstruction([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_queue_reconstruction()
    print(f"Queue Reconstruction by Height Sort Insert 100 iterations took {t*1000:.3f}ms")
