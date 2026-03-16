"""Benchmark profile for Subarray Sums Divisible by K."""
import time
from src.arrays_and_hashing.subarray_divisible_k import SubarraySumsDivisibleByK

def benchmark():
    solver = SubarraySumsDivisibleByK()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
