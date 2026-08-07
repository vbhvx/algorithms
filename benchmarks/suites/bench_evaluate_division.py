"""
Empirical benchmark for Evaluate Division Weighted Graph DFS
"""
import time
from algorithms.practice.graphs_and_traversals.evaluate_division import solve_evaluate_division

def benchmark_evaluate_division():
    start = time.perf_counter()
    for _ in range(100):
        solve_evaluate_division([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_evaluate_division()
    print(f"Evaluate Division Weighted Graph DFS 100 iterations took {t*1000:.3f}ms")
