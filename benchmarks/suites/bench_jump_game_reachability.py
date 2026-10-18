"""
Empirical benchmark for Jump Game Maximum Reachable Index
"""
import time
from algorithms.practice.greedy_algorithms.jump_game_reachability import solve_jump_game_reachability

def benchmark_jump_game_reachability():
    start = time.perf_counter()
    for _ in range(100):
        solve_jump_game_reachability([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_jump_game_reachability()
    print(f"Jump Game Maximum Reachable Index 100 iterations took {t*1000:.3f}ms")
