"""
Empirical benchmark for Path Sum II All Root to Leaf Target Paths
"""
import time
from algorithms.practice.trees_and_bst.path_sum_ii import solve_path_sum_ii

def benchmark_path_sum_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_path_sum_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_path_sum_ii()
    print(f"Path Sum II All Root to Leaf Target Paths 100 iterations took {t*1000:.3f}ms")
