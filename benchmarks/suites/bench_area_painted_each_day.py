"""
Empirical benchmark for Amount of New Area Painted Each Day DSU Jump
"""
import time
from algorithms.practice.intervals_scheduling.area_painted_each_day import solve_area_painted_each_day

def benchmark_area_painted_each_day():
    start = time.perf_counter()
    for _ in range(100):
        solve_area_painted_each_day([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_area_painted_each_day()
    print(f"Amount of New Area Painted Each Day DSU Jump 100 iterations took {t*1000:.3f}ms")
