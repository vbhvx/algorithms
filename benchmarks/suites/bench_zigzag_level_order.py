"""
Empirical benchmark for Binary Tree Zigzag Level Order Traversal
"""
import time
from algorithms.practice.trees_and_bst.zigzag_level_order import solve_zigzag_level_order

def benchmark_zigzag_level_order():
    start = time.perf_counter()
    for _ in range(100):
        solve_zigzag_level_order([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_zigzag_level_order()
    print(f"Binary Tree Zigzag Level Order Traversal 100 iterations took {t*1000:.3f}ms")
