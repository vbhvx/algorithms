"""
Empirical benchmark for Basic Calculator II Precedence Stack
"""
import time
from algorithms.practice.stack_and_queue.basic_calculator_ii import solve_basic_calculator_ii

def benchmark_basic_calculator_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_basic_calculator_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_basic_calculator_ii()
    print(f"Basic Calculator II Precedence Stack 100 iterations took {t*1000:.3f}ms")
