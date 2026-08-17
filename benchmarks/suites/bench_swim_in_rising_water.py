"""
Empirical benchmark for Swim in Rising Water Dijkstra Grid Elevation
"""
import time
from algorithms.practice.shortest_paths.swim_in_rising_water import solve_swim_in_rising_water

def benchmark_swim_in_rising_water():
    start = time.perf_counter()
    for _ in range(100):
        solve_swim_in_rising_water([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_swim_in_rising_water()
    print(f"Swim in Rising Water Dijkstra Grid Elevation 100 iterations took {t*1000:.3f}ms")
