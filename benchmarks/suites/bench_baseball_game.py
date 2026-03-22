"""
Empirical benchmark for Baseball Game Record Stack
"""
import time
from algorithms.practice.stack_and_queue.baseball_game import solve_baseball_game

def benchmark_baseball_game():
    start = time.perf_counter()
    for _ in range(100):
        solve_baseball_game([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_baseball_game()
    print(f"Baseball Game Record Stack 100 iterations took {t*1000:.3f}ms")
