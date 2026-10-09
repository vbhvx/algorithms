"""
Empirical benchmark for House Robber III Include Exclude Subtree
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.house_robber_iii_tree import solve_house_robber_iii_tree

def benchmark_house_robber_iii_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_house_robber_iii_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_house_robber_iii_tree()
    print(f"House Robber III Include Exclude Subtree 100 iterations took {t*1000:.3f}ms")
