"""
Empirical benchmark for Binary Tree Level Order Traversal BFS
"""
import time
from algorithms.practice.trees_and_bst.level_order_traversal import solve_level_order_traversal

def benchmark_level_order_traversal():
    start = time.perf_counter()
    for _ in range(100):
        solve_level_order_traversal([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_level_order_traversal()
    print(f"Binary Tree Level Order Traversal BFS 100 iterations took {t*1000:.3f}ms")
