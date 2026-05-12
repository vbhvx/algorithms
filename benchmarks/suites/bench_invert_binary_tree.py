"""
Empirical benchmark for Invert Binary Tree Recursive DFS
"""
import time
from algorithms.practice.trees_and_bst.invert_binary_tree import solve_invert_binary_tree

def benchmark_invert_binary_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_invert_binary_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_invert_binary_tree()
    print(f"Invert Binary Tree Recursive DFS 100 iterations took {t*1000:.3f}ms")
