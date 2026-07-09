"""
Empirical benchmark for Refill Water Plants Capacity Priority Queue
"""
import time
from algorithms.practice.heaps_and_priority.refill_water_bottles import solve_refill_water_bottles

def benchmark_refill_water_bottles():
    start = time.perf_counter()
    for _ in range(100):
        solve_refill_water_bottles([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_refill_water_bottles()
    print(f"Refill Water Plants Capacity Priority Queue 100 iterations took {t*1000:.3f}ms")
