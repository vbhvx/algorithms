"""
Empirical benchmark for Kth Smallest Spanning Tree Edge Exchange
"""
import time
from algorithms.practice.minimum_spanning_trees.k_minimum_spanning_tree import solve_k_minimum_spanning_tree

def benchmark_k_minimum_spanning_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_k_minimum_spanning_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_k_minimum_spanning_tree()
    print(f"Kth Smallest Spanning Tree Edge Exchange 100 iterations took {t*1000:.3f}ms")
