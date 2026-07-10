"""
Empirical benchmark for Swim in Rising Water Dijkstra Priority Queue
"""
import time
from algorithms.practice.heaps_and_priority.swim_rising_water_heap import solve_swim_rising_water_heap

def benchmark_swim_rising_water_heap():
    start = time.perf_counter()
    for _ in range(100):
        solve_swim_rising_water_heap([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_swim_rising_water_heap()
    print(f"Swim in Rising Water Dijkstra Priority Queue 100 iterations took {t*1000:.3f}ms")
