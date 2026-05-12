"""
Empirical benchmark for Minimum Depth of Binary Tree BFS
"""
import time
from algorithms.practice.trees_and_bst.min_depth_tree import solve_min_depth_tree

def benchmark_min_depth_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_depth_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_depth_tree()
    print(f"Minimum Depth of Binary Tree BFS 100 iterations took {t*1000:.3f}ms")
