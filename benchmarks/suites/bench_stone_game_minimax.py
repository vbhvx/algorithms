"""
Empirical benchmark for Stone Game Minimax Dynamic Programming
"""
import time
from algorithms.practice.dynamic_programming_2d.stone_game_minimax import solve_stone_game_minimax

def benchmark_stone_game_minimax():
    start = time.perf_counter()
    for _ in range(100):
        solve_stone_game_minimax([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stone_game_minimax()
    print(f"Stone Game Minimax Dynamic Programming 100 iterations took {t*1000:.3f}ms")
