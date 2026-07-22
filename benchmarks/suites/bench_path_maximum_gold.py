"""
Empirical benchmark for Path with Maximum Gold DFS Matrix Visited
"""
import time
from algorithms.practice.backtracking.path_maximum_gold import solve_path_maximum_gold

def benchmark_path_maximum_gold():
    start = time.perf_counter()
    for _ in range(100):
        solve_path_maximum_gold([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_path_maximum_gold()
    print(f"Path with Maximum Gold DFS Matrix Visited 100 iterations took {t*1000:.3f}ms")
