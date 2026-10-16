"""
Empirical benchmark for Sum of Distances in Tree Rerooting DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.tree_rerooting_sum_dist import solve_tree_rerooting_sum_dist

def benchmark_tree_rerooting_sum_dist():
    start = time.perf_counter()
    for _ in range(100):
        solve_tree_rerooting_sum_dist([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_tree_rerooting_sum_dist()
    print(f"Sum of Distances in Tree Rerooting DP 100 iterations took {t*1000:.3f}ms")
