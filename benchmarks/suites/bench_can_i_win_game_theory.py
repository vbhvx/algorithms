"""
Empirical benchmark for Can I Win Minimax Game Theory Bitmask
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.can_i_win_game_theory import solve_can_i_win_game_theory

def benchmark_can_i_win_game_theory():
    start = time.perf_counter()
    for _ in range(100):
        solve_can_i_win_game_theory([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_can_i_win_game_theory()
    print(f"Can I Win Minimax Game Theory Bitmask 100 iterations took {t*1000:.3f}ms")
