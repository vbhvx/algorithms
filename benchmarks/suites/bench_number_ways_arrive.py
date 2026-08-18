"""
Empirical benchmark for Number of Ways to Arrive at Destination Dijkstra DP
"""
import time
from algorithms.practice.shortest_paths.number_ways_arrive import solve_number_ways_arrive

def benchmark_number_ways_arrive():
    start = time.perf_counter()
    for _ in range(100):
        solve_number_ways_arrive([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_number_ways_arrive()
    print(f"Number of Ways to Arrive at Destination Dijkstra DP 100 iterations took {t*1000:.3f}ms")
