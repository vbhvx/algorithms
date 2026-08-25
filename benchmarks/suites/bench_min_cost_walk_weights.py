"""
Empirical benchmark for Minimum Cost Walk in Weighted Graph Bitwise AND
"""
import time
from algorithms.practice.minimum_spanning_trees.min_cost_walk_weights import solve_min_cost_walk_weights

def benchmark_min_cost_walk_weights():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_walk_weights([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_walk_weights()
    print(f"Minimum Cost Walk in Weighted Graph Bitwise AND 100 iterations took {t*1000:.3f}ms")
