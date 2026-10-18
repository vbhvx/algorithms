"""
Empirical benchmark for Jump Game II Minimum Jumps Current Range
"""
import time
from algorithms.practice.greedy_algorithms.jump_game_ii_bfs import solve_jump_game_ii_bfs

def benchmark_jump_game_ii_bfs():
    start = time.perf_counter()
    for _ in range(100):
        solve_jump_game_ii_bfs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_jump_game_ii_bfs()
    print(f"Jump Game II Minimum Jumps Current Range 100 iterations took {t*1000:.3f}ms")
