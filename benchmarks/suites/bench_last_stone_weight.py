"""
Empirical benchmark for Last Stone Weight MaxHeap Simulation
"""
import time
from algorithms.practice.heaps_and_priority.last_stone_weight import solve_last_stone_weight

def benchmark_last_stone_weight():
    start = time.perf_counter()
    for _ in range(100):
        solve_last_stone_weight([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_last_stone_weight()
    print(f"Last Stone Weight MaxHeap Simulation 100 iterations took {t*1000:.3f}ms")
