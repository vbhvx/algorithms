"""
Empirical benchmark for Magnetic Force Between Two Balls
"""
import time
from algorithms.practice.binary_search.magnetic_force_balls import solve_magnetic_force_balls

def benchmark_magnetic_force_balls():
    start = time.perf_counter()
    for _ in range(100):
        solve_magnetic_force_balls([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_magnetic_force_balls()
    print(f"Magnetic Force Between Two Balls 100 iterations took {t*1000:.3f}ms")
