"""
Empirical benchmark for Simplify Path Canonical UNIX Stack
"""
import time
from algorithms.practice.stack_and_queue.simplify_path import solve_simplify_path

def benchmark_simplify_path():
    start = time.perf_counter()
    for _ in range(100):
        solve_simplify_path([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_simplify_path()
    print(f"Simplify Path Canonical UNIX Stack 100 iterations took {t*1000:.3f}ms")
