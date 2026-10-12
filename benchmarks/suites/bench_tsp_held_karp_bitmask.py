"""
Empirical benchmark for Travelling Salesperson Held-Karp Algorithm
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.tsp_held_karp_bitmask import solve_tsp_held_karp_bitmask

def benchmark_tsp_held_karp_bitmask():
    start = time.perf_counter()
    for _ in range(100):
        solve_tsp_held_karp_bitmask([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_tsp_held_karp_bitmask()
    print(f"Travelling Salesperson Held-Karp Algorithm 100 iterations took {t*1000:.3f}ms")
