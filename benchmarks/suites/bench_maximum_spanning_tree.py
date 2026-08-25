"""
Empirical benchmark for Maximum Spanning Tree Inverted Weights
"""
import time
from algorithms.practice.minimum_spanning_trees.maximum_spanning_tree import solve_maximum_spanning_tree

def benchmark_maximum_spanning_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximum_spanning_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximum_spanning_tree()
    print(f"Maximum Spanning Tree Inverted Weights 100 iterations took {t*1000:.3f}ms")
