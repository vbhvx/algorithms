"""
Empirical benchmark for Remove All Adjacent Duplicates
"""
import time
from algorithms.practice.stack_and_queue.remove_adj_duplicates import solve_remove_adj_duplicates

def benchmark_remove_adj_duplicates():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_adj_duplicates([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_adj_duplicates()
    print(f"Remove All Adjacent Duplicates 100 iterations took {t*1000:.3f}ms")
