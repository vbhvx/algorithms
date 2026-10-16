"""
Empirical benchmark for Maximum Product of Splitted Binary Tree
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.maximum_product_tree_split import solve_maximum_product_tree_split

def benchmark_maximum_product_tree_split():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximum_product_tree_split([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximum_product_tree_split()
    print(f"Maximum Product of Splitted Binary Tree 100 iterations took {t*1000:.3f}ms")
