"""
Empirical benchmark for Matchsticks to Square 4 Equal Sums
"""
import time
from algorithms.practice.backtracking.matchsticks_to_square import solve_matchsticks_to_square

def benchmark_matchsticks_to_square():
    start = time.perf_counter()
    for _ in range(100):
        solve_matchsticks_to_square([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_matchsticks_to_square()
    print(f"Matchsticks to Square 4 Equal Sums 100 iterations took {t*1000:.3f}ms")
