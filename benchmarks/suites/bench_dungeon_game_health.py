"""
Empirical benchmark for Dungeon Game Bottom-Up Knight Health
"""
import time
from algorithms.practice.dynamic_programming_2d.dungeon_game_health import solve_dungeon_game_health

def benchmark_dungeon_game_health():
    start = time.perf_counter()
    for _ in range(100):
        solve_dungeon_game_health([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dungeon_game_health()
    print(f"Dungeon Game Bottom-Up Knight Health 100 iterations took {t*1000:.3f}ms")
