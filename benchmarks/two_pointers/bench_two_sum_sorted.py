"""Benchmark profile for Two Sum II Sorted Pointers."""
import time
from src.two_pointers.two_sum_sorted import TwoSumIiSortedPointers

def benchmark():
    solver = TwoSumIiSortedPointers()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
