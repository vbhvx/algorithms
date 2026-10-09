"""
Empirical benchmark for Diameter of General Tree Rerooting DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.tree_diameter_general import solve_tree_diameter_general

def benchmark_tree_diameter_general():
    start = time.perf_counter()
    for _ in range(100):
        solve_tree_diameter_general([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_tree_diameter_general()
    print(f"Diameter of General Tree Rerooting DP 100 iterations took {t*1000:.3f}ms")
