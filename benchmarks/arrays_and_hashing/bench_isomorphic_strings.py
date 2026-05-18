"""Benchmark profile for Isomorphic Strings Bijective."""
import time
from src.arrays_and_hashing.isomorphic_strings import IsomorphicStringsBijective

def benchmark():
    solver = IsomorphicStringsBijective()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
