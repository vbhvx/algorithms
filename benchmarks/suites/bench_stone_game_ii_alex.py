"""
Empirical benchmark for Stone Game II Suffix Sums Minimax
"""
import time
from algorithms.practice.dynamic_programming_2d.stone_game_ii_alex import solve_stone_game_ii_alex

def benchmark_stone_game_ii_alex():
    start = time.perf_counter()
    for _ in range(100):
        solve_stone_game_ii_alex([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stone_game_ii_alex()
    print(f"Stone Game II Suffix Sums Minimax 100 iterations took {t*1000:.3f}ms")
