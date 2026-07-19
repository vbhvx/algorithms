"""
Empirical benchmark for Find Unique Binary String Cantor Diagonal
"""
import time
from algorithms.practice.backtracking.find_unique_binary import solve_find_unique_binary

def benchmark_find_unique_binary():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_unique_binary([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_unique_binary()
    print(f"Find Unique Binary String Cantor Diagonal 100 iterations took {t*1000:.3f}ms")
