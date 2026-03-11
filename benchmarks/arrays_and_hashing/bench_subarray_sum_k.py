"""Benchmark profile for Subarray Sum Equals K Prefix Map."""
import time
from src.arrays_and_hashing.subarray_sum_k import SubarraySumEqualsKPrefixMap

def benchmark():
    solver = SubarraySumEqualsKPrefixMap()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
