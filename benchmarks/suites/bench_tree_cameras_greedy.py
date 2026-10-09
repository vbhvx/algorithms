"""
Empirical benchmark for Binary Tree Cameras Tree DP Vertex Cover
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.tree_cameras_greedy import solve_tree_cameras_greedy

def benchmark_tree_cameras_greedy():
    start = time.perf_counter()
    for _ in range(100):
        solve_tree_cameras_greedy([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_tree_cameras_greedy()
    print(f"Binary Tree Cameras Tree DP Vertex Cover 100 iterations took {t*1000:.3f}ms")
