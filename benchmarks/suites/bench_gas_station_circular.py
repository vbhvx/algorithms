"""
Empirical benchmark for Gas Station Starting Point Tank Deficit
"""
import time
from algorithms.practice.greedy_algorithms.gas_station_circular import solve_gas_station_circular

def benchmark_gas_station_circular():
    start = time.perf_counter()
    for _ in range(100):
        solve_gas_station_circular([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_gas_station_circular()
    print(f"Gas Station Starting Point Tank Deficit 100 iterations took {t*1000:.3f}ms")
