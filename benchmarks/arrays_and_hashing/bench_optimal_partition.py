"""Benchmark profile for Optimal Partition of String."""
import time
from src.arrays_and_hashing.optimal_partition import OptimalPartitionOfString

def benchmark():
    solver = OptimalPartitionOfString()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
