"""Benchmark profile for First Missing Positive In Place."""
import time
from src.arrays_and_hashing.first_missing_positive import FirstMissingPositiveInPlace

def benchmark():
    solver = FirstMissingPositiveInPlace()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
