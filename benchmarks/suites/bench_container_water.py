"""
Empirical benchmark for Container With Most Water
"""
import time
from algorithms.practice.two_pointers.container_water import solve_container_water

def benchmark_container_water():
    start = time.perf_counter()
    for _ in range(100):
        solve_container_water([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_container_water()
    print(f"Container With Most Water 100 iterations took {t*1000:.3f}ms")
