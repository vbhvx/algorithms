"""
Empirical benchmark for Beautiful Arrangement Divisibility Backtrack
"""
import time
from algorithms.practice.backtracking.beautiful_arrangement import solve_beautiful_arrangement

def benchmark_beautiful_arrangement():
    start = time.perf_counter()
    for _ in range(100):
        solve_beautiful_arrangement([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_beautiful_arrangement()
    print(f"Beautiful Arrangement Divisibility Backtrack 100 iterations took {t*1000:.3f}ms")
