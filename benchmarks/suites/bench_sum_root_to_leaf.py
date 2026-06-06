"""
Empirical benchmark for Sum Root to Leaf Numbers Decimal Shift
"""
import time
from algorithms.practice.trees_and_bst.sum_root_to_leaf import solve_sum_root_to_leaf

def benchmark_sum_root_to_leaf():
    start = time.perf_counter()
    for _ in range(100):
        solve_sum_root_to_leaf([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sum_root_to_leaf()
    print(f"Sum Root to Leaf Numbers Decimal Shift 100 iterations took {t*1000:.3f}ms")
