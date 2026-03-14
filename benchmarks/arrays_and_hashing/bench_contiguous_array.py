"""Benchmark profile for Contiguous Array Equal 0 1."""
import time
from src.arrays_and_hashing.contiguous_array import ContiguousArrayEqual01

def benchmark():
    solver = ContiguousArrayEqual01()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
