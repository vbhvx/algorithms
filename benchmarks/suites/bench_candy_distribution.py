"""
Empirical benchmark for Candy Distribution Left Right Pass Peak
"""
import time
from algorithms.practice.greedy_algorithms.candy_distribution import solve_candy_distribution

def benchmark_candy_distribution():
    start = time.perf_counter()
    for _ in range(100):
        solve_candy_distribution([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_candy_distribution()
    print(f"Candy Distribution Left Right Pass Peak 100 iterations took {t*1000:.3f}ms")
