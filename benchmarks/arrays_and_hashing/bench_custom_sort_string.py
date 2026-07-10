"""Benchmark profile for Custom Sort String Frequency."""
import time
from src.arrays_and_hashing.custom_sort_string import CustomSortStringFrequency

def benchmark():
    solver = CustomSortStringFrequency()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
