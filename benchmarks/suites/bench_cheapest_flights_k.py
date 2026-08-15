"""
Empirical benchmark for Cheapest Flights Within K Stops Bellman Ford
"""
import time
from algorithms.practice.shortest_paths.cheapest_flights_k import solve_cheapest_flights_k

def benchmark_cheapest_flights_k():
    start = time.perf_counter()
    for _ in range(100):
        solve_cheapest_flights_k([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_cheapest_flights_k()
    print(f"Cheapest Flights Within K Stops Bellman Ford 100 iterations took {t*1000:.3f}ms")
