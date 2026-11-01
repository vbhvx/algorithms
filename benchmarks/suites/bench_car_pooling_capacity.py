"""
Empirical benchmark for Car Pooling Difference Array Capacity Sweep
"""
import time
from algorithms.practice.intervals_scheduling.car_pooling_capacity import solve_car_pooling_capacity

def benchmark_car_pooling_capacity():
    start = time.perf_counter()
    for _ in range(100):
        solve_car_pooling_capacity([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_car_pooling_capacity()
    print(f"Car Pooling Difference Array Capacity Sweep 100 iterations took {t*1000:.3f}ms")
