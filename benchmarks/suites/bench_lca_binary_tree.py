"""
Empirical benchmark for Lowest Common Ancestor Binary Tree Postorder
"""
import time
from algorithms.practice.trees_and_bst.lca_binary_tree import solve_lca_binary_tree

def benchmark_lca_binary_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_lca_binary_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_lca_binary_tree()
    print(f"Lowest Common Ancestor Binary Tree Postorder 100 iterations took {t*1000:.3f}ms")
