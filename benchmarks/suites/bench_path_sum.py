"""
Empirical benchmark for Path Sum Target Root to Leaf
"""
import time
from algorithms.practice.trees_and_bst.path_sum import solve_path_sum

def benchmark_path_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_path_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_path_sum()
    print(f"Path Sum Target Root to Leaf 100 iterations took {t*1000:.3f}ms")
