"""
Empirical benchmark for Remove Duplicates Sorted Array II
"""
import time
from algorithms.practice.two_pointers.remove_duplicates_ii import solve_remove_duplicates_ii

def benchmark_remove_duplicates_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_duplicates_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_duplicates_ii()
    print(f"Remove Duplicates Sorted Array II 100 iterations took {t*1000:.3f}ms")
