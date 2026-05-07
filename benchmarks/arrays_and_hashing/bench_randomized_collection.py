"""Benchmark profile for Insert Delete GetRandom Duplicates."""
import time
from src.arrays_and_hashing.randomized_collection import InsertDeleteGetrandomDuplicates

def benchmark():
    solver = InsertDeleteGetrandomDuplicates()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
