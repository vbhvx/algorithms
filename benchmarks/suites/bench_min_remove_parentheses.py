"""
Empirical benchmark for Minimum Remove to Make Valid Parentheses
"""
import time
from algorithms.practice.stack_and_queue.min_remove_parentheses import solve_min_remove_parentheses

def benchmark_min_remove_parentheses():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_remove_parentheses([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_remove_parentheses()
    print(f"Minimum Remove to Make Valid Parentheses 100 iterations took {t*1000:.3f}ms")
