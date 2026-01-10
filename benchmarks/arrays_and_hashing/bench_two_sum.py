"""Benchmark profile for Two Sum Hash Map."""
import time
from src.arrays_and_hashing.two_sum import TwoSumHashMap

def benchmark():
    solver = TwoSumHashMap()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
