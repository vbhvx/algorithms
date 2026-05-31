"""
Empirical benchmark for Path Sum III Subpath Prefix Sum Map
"""
import time
from algorithms.practice.trees_and_bst.path_sum_iii import solve_path_sum_iii

def benchmark_path_sum_iii():
    start = time.perf_counter()
    for _ in range(100):
        solve_path_sum_iii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_path_sum_iii()
    print(f"Path Sum III Subpath Prefix Sum Map 100 iterations took {t*1000:.3f}ms")
