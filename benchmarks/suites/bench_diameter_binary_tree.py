"""
Empirical benchmark for Diameter of Binary Tree Postorder
"""
import time
from algorithms.practice.trees_and_bst.diameter_binary_tree import solve_diameter_binary_tree

def benchmark_diameter_binary_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_diameter_binary_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_diameter_binary_tree()
    print(f"Diameter of Binary Tree Postorder 100 iterations took {t*1000:.3f}ms")
