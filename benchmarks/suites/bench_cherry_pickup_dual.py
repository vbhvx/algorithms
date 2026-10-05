"""
Empirical benchmark for Cherry Pickup Dual Walk Dynamic Programming
"""
import time
from algorithms.practice.dynamic_programming_2d.cherry_pickup_dual import solve_cherry_pickup_dual

def benchmark_cherry_pickup_dual():
    start = time.perf_counter()
    for _ in range(100):
        solve_cherry_pickup_dual([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_cherry_pickup_dual()
    print(f"Cherry Pickup Dual Walk Dynamic Programming 100 iterations took {t*1000:.3f}ms")
