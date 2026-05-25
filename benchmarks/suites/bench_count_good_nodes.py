"""
Empirical benchmark for Count Good Nodes in Binary Tree Max Path
"""
import time
from algorithms.practice.trees_and_bst.count_good_nodes import solve_count_good_nodes

def benchmark_count_good_nodes():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_good_nodes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_good_nodes()
    print(f"Count Good Nodes in Binary Tree Max Path 100 iterations took {t*1000:.3f}ms")
