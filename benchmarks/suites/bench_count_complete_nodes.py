"""
Empirical benchmark for Count Complete Tree Nodes Log Squared
"""
import time
from algorithms.practice.trees_and_bst.count_complete_nodes import solve_count_complete_nodes

def benchmark_count_complete_nodes():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_complete_nodes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_complete_nodes()
    print(f"Count Complete Tree Nodes Log Squared 100 iterations took {t*1000:.3f}ms")
