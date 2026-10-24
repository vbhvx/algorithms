"""
Empirical benchmark for Dota2 Senate Round-Robin Queue Elimination
"""
import time
from algorithms.practice.greedy_algorithms.dota2_senate_queue import solve_dota2_senate_queue

def benchmark_dota2_senate_queue():
    start = time.perf_counter()
    for _ in range(100):
        solve_dota2_senate_queue([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dota2_senate_queue()
    print(f"Dota2 Senate Round-Robin Queue Elimination 100 iterations took {t*1000:.3f}ms")
