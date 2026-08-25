"""
Empirical benchmark for Minimum Bottleneck Spanning Tree Verification
"""
import time
from algorithms.practice.minimum_spanning_trees.bottleneck_spanning_tree import solve_bottleneck_spanning_tree

def benchmark_bottleneck_spanning_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_bottleneck_spanning_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bottleneck_spanning_tree()
    print(f"Minimum Bottleneck Spanning Tree Verification 100 iterations took {t*1000:.3f}ms")
