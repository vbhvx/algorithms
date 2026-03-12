"""
Empirical benchmark for Car Fleet Monotonic Collision
"""
import time
from algorithms.practice.stack_and_queue.car_fleet import solve_car_fleet

def benchmark_car_fleet():
    start = time.perf_counter()
    for _ in range(100):
        solve_car_fleet([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_car_fleet()
    print(f"Car Fleet Monotonic Collision 100 iterations took {t*1000:.3f}ms")
