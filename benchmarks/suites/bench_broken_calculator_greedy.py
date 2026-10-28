"""
Empirical benchmark for Broken Calculator Reverse Backward Operations
"""
import time
from algorithms.practice.greedy_algorithms.broken_calculator_greedy import solve_broken_calculator_greedy

def benchmark_broken_calculator_greedy():
    start = time.perf_counter()
    for _ in range(100):
        solve_broken_calculator_greedy([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_broken_calculator_greedy()
    print(f"Broken Calculator Reverse Backward Operations 100 iterations took {t*1000:.3f}ms")
