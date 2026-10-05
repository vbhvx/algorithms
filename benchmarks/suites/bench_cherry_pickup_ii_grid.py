"""
Empirical benchmark for Cherry Pickup II Two Robots Simultaneous
"""
import time
from algorithms.practice.dynamic_programming_2d.cherry_pickup_ii_grid import solve_cherry_pickup_ii_grid

def benchmark_cherry_pickup_ii_grid():
    start = time.perf_counter()
    for _ in range(100):
        solve_cherry_pickup_ii_grid([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_cherry_pickup_ii_grid()
    print(f"Cherry Pickup II Two Robots Simultaneous 100 iterations took {t*1000:.3f}ms")
