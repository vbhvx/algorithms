"""
Empirical benchmark for Boats to Save People Heaviest Lightest Pair
"""
import time
from algorithms.practice.greedy_algorithms.boats_to_save_people import solve_boats_to_save_people

def benchmark_boats_to_save_people():
    start = time.perf_counter()
    for _ in range(100):
        solve_boats_to_save_people([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_boats_to_save_people()
    print(f"Boats to Save People Heaviest Lightest Pair 100 iterations took {t*1000:.3f}ms")
