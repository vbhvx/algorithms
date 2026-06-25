"""Benchmark profile for Contains Duplicate II Window Hash."""
import time
from src.arrays_and_hashing.contains_duplicate_ii import ContainsDuplicateIiWindowHash

def benchmark():
    solver = ContainsDuplicateIiWindowHash()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
