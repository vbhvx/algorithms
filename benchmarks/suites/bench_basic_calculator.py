"""
Empirical benchmark for Basic Calculator Recursive Parentheses
"""
import time
from algorithms.practice.stack_and_queue.basic_calculator import solve_basic_calculator

def benchmark_basic_calculator():
    start = time.perf_counter()
    for _ in range(100):
        solve_basic_calculator([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_basic_calculator()
    print(f"Basic Calculator Recursive Parentheses 100 iterations took {t*1000:.3f}ms")
