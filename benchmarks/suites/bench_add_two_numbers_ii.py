"""
Empirical benchmark for Add Two Numbers II Most Significant Stack
"""
import time
from algorithms.practice.linked_lists.add_two_numbers_ii import solve_add_two_numbers_ii

def benchmark_add_two_numbers_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_add_two_numbers_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_add_two_numbers_ii()
    print(f"Add Two Numbers II Most Significant Stack 100 iterations took {t*1000:.3f}ms")
