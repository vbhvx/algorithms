"""Benchmark profile for 3Sum Closest Target Sum."""
import time
from src.two_pointers.three_sum_closest import 3SumClosestTargetSum

def benchmark():
    solver = 3SumClosestTargetSum()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
