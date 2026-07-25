"""
Empirical benchmark for Expression Add Operators Precedence Backtrack
"""
import time
from algorithms.practice.backtracking.expression_add_ops import solve_expression_add_ops

def benchmark_expression_add_ops():
    start = time.perf_counter()
    for _ in range(100):
        solve_expression_add_ops([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_expression_add_ops()
    print(f"Expression Add Operators Precedence Backtrack 100 iterations took {t*1000:.3f}ms")
