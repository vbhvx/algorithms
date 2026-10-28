"""
Empirical benchmark for Two City Scheduling Opportunity Cost Sort
"""
import time
from algorithms.practice.greedy_algorithms.two_city_scheduling import solve_two_city_scheduling

def benchmark_two_city_scheduling():
    start = time.perf_counter()
    for _ in range(100):
        solve_two_city_scheduling([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_two_city_scheduling()
    print(f"Two City Scheduling Opportunity Cost Sort 100 iterations took {t*1000:.3f}ms")
