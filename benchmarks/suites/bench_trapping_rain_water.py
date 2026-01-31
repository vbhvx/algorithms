"""
Empirical benchmark for Trapping Rain Water Max Bounds
"""
import time
from algorithms.practice.two_pointers.trapping_rain_water import solve_trapping_rain_water

def benchmark_trapping_rain_water():
    start = time.perf_counter()
    for _ in range(100):
        solve_trapping_rain_water([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_trapping_rain_water()
    print(f"Trapping Rain Water Max Bounds 100 iterations took {t*1000:.3f}ms")
