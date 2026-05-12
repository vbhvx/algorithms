"""
Empirical benchmark for Maximum Depth of Binary Tree
"""
import time
from algorithms.practice.trees_and_bst.max_depth_tree import solve_max_depth_tree

def benchmark_max_depth_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_depth_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_depth_tree()
    print(f"Maximum Depth of Binary Tree 100 iterations took {t*1000:.3f}ms")
